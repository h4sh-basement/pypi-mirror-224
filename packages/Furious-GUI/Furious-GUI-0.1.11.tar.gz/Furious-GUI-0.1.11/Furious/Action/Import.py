from Furious.Core.Configuration import (
    Configuration,
    XrayCoreConfiguration,
    ProxyOutboundObject,
    ProxyOutboundObjectSS,
)
from Furious.Gui.Action import Action
from Furious.Widget.Widget import Menu, MessageBox
from Furious.Utility.Constants import APP
from Furious.Utility.Utility import (
    Base64Encoder,
    Protocol,
    StateContext,
    ServerStorage,
    bootstrapIcon,
    protocolRepr,
)
from Furious.Utility.Translator import gettext as _

from PySide6.QtWidgets import QApplication

import re
import ujson
import logging
import urllib.parse

logger = logging.getLogger(__name__)


class ImportErrorBox(MessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def retranslate(self):
        with StateContext(self):
            self.setWindowTitle(_(self.windowTitle()))
            self.setText(_(self.text()))

            # Ignore informative text, buttons

            self.moveToCenter()


class JSONImportOKBox(MessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(_('Import'))
        self.setText(_('Import JSON configuration success.'))

        self.addButton(_('Go to edit'), MessageBox.ButtonRole.AcceptRole)
        self.addButton(_('OK'), MessageBox.ButtonRole.RejectRole)


class LinkImportOKBox(MessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.remark = ''

        self.setWindowTitle(_('Import'))

        self.addButton(_('Go to edit'), MessageBox.ButtonRole.AcceptRole)
        self.addButton(_('OK'), MessageBox.ButtonRole.RejectRole)

    def getText(self):
        if self.remark:
            return _('Import share link success: ') + f'{self.remark}'
        else:
            return _('Import share link success.')

    def retranslate(self):
        self.setWindowTitle(_(self.windowTitle()))
        self.setText(self.getText())

        # Ignore informative text

        for button in self.buttons():
            button.setText(_(button.text()))

        self.moveToCenter()


class ImportLinkResultBox(MessageBox):
    def __init__(self, successRemark, rowCount, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.successRemark = successRemark
        self.rowCount = rowCount

        self.setWindowTitle(_('Import'))
        self.setIcon(MessageBox.Icon.Information)
        self.setText(self.getText())

    def getText(self):
        return (
            _('Import share link success: ')
            + f'\n\n'
            + '\n'.join(
                list(
                    f'{index + 1} - {remark}. {_("Imported to row")} {self.rowCount + index + 1}'
                    for index, remark in enumerate(self.successRemark)
                )
            )
        )

    def retranslate(self):
        with StateContext(self):
            self.setWindowTitle(_(self.windowTitle()))
            self.setText(self.getText())

            # Ignore informative text, buttons

            self.moveToCenter()


class ImportLinkAction(Action):
    def __init__(self, **kwargs):
        super().__init__(_('Import Share Link From Clipboard'), **kwargs)

        self.clipboard = ''

        self.linkErrorBox = ImportErrorBox(icon=MessageBox.Icon.Critical)
        self.linkImportOK = LinkImportOKBox(icon=MessageBox.Icon.Information)

    def showLinkErrorBox(self):
        self.linkErrorBox.setWindowTitle(_('Import'))
        if len(self.clipboard) > 1000:
            self.linkErrorBox.setText(_('Invalid share link.'))
            self.linkErrorBox.setInformativeText('')
        else:
            self.linkErrorBox.setText(
                _('Invalid share link. The content of the clipboard is:')
            )
            self.linkErrorBox.setInformativeText(self.clipboard)

        # Show the MessageBox and wait for user to close it
        self.linkErrorBox.exec()

    def showLinkImportOK(self, remark):
        self.linkImportOK.remark = remark
        self.linkImportOK.setText(self.linkImportOK.getText())

        # Show the MessageBox and wait for user to close it
        choice = self.linkImportOK.exec()

        if choice == MessageBox.ButtonRole.AcceptRole.value:
            # Go to edit
            APP().MainWidget.show()
        else:
            # OK. Do nothing
            pass

    def parseShareLinkVMess(self, data, isV2rayN):
        if isV2rayN:

            def getOrDefault(key, default=''):
                return data.get(key, default)

            try:
                # Ignore: v
                myJSON = XrayCoreConfiguration.build(
                    ProxyOutboundObject(
                        'vmess',
                        getOrDefault('add'),
                        int(getOrDefault('port', '0')),
                        getOrDefault('id'),
                        getOrDefault('scy', 'auto'),
                        getOrDefault('net', 'tcp'),
                        getOrDefault('tls', 'none'),
                        # kwargs. V2rayN share standard -> (VMess AEAD / VLESS) standard
                        aid=int(getOrDefault('aid', '0')),
                        headerType=getOrDefault('type', 'none'),
                        host=getOrDefault('host'),
                        quicSecurity=getOrDefault('host', 'none'),
                        path=getOrDefault('path'),
                        key=getOrDefault('path'),
                        seed=getOrDefault('path'),
                        serviceName=getOrDefault('path'),
                        sni=getOrDefault('sni'),
                        alpn=getOrDefault('alpn'),
                        # Note: If specify default value 'chrome', some share link fails.
                        # Leave default value as empty
                        fp=getOrDefault('fp'),
                    )
                )

                remark = urllib.parse.unquote(getOrDefault('ps'))

                APP().MainWidget.importServer(
                    remark,
                    ujson.dumps(
                        myJSON,
                        indent=2,
                        ensure_ascii=False,
                        escape_forward_slashes=False,
                    ),
                )

                logger.info(
                    'import share link from clipboard success. '
                    f'Remark: {remark}. Protocol: VMess. (V2rayN share standard)'
                )

                return remark, True

            except Exception:
                # Any non-exit exceptions

                return '', False
        else:
            return self.parseShareLinkStandard('vmess', data)

    @staticmethod
    def parseShareLinkStandard(protocol, data):
        try:
            parseResult = urllib.parse.urlparse(data)

            queryObject = {
                key: value for key, value in urllib.parse.parse_qsl(parseResult.query)
            }

            remark = urllib.parse.unquote(parseResult.fragment)

            uuid_, remote_host, remote_port = re.split(r'[@:]', parseResult.netloc)

            encryption = queryObject.get('encryption', 'none')
            type_ = queryObject.get('type', 'tcp')
            security = queryObject.get('security', 'none')

            # Remove redundant items
            queryObject.pop('encryption', '')
            queryObject.pop('type', '')
            queryObject.pop('security', '')

            myJSON = XrayCoreConfiguration.build(
                ProxyOutboundObject(
                    protocol,
                    remote_host,
                    int(remote_port),
                    uuid_,
                    encryption,
                    type_,
                    security,
                    # kwargs
                    **queryObject,
                )
            )

            APP().MainWidget.importServer(
                remark,
                ujson.dumps(
                    myJSON, indent=2, ensure_ascii=False, escape_forward_slashes=False
                ),
            )

            logger.info(
                f'import share link from clipboard success. '
                f'Remark: {remark}. Protocol: {protocolRepr(protocol)}'
            )

            return remark, True
        except Exception:
            # Any non-exit exceptions

            return '', False

    @staticmethod
    def parseShareLinkSIP002(data):
        try:
            result = urllib.parse.urlparse(data)
            remark = urllib.parse.unquote(result.fragment)

            try:
                # Try pack with 3 element
                userinfo, address, port = re.split(r'[@:]', result.netloc)

                # Some old SS share link doesn't add padding
                # in base64 encoding. Add padding to userinfo
                method, password = (
                    Base64Encoder.decode(userinfo + '===').decode().split(':')
                )
            except ValueError:
                # Unpack error. Try pack with 4 element

                method, password, address, port = re.split(r'[@:]', result.netloc)
            except Exception as ex:
                # Any non-exit exceptions

                raise ex

            myJSON = XrayCoreConfiguration.build(
                ProxyOutboundObjectSS(
                    urllib.parse.unquote(method),
                    urllib.parse.unquote(password),
                    address,
                    port,
                )
            )

            APP().MainWidget.importServer(
                remark,
                ujson.dumps(
                    myJSON, indent=2, ensure_ascii=False, escape_forward_slashes=False
                ),
            )

            logger.info(
                f'import share link from clipboard success. '
                f'Remark: {remark}. Protocol: {Protocol.Shadowsocks}'
            )

            return remark, True
        except Exception as ex:
            # Any non-exit exceptions

            return '', False

    def parseShareLinkSS(self, data):
        try:
            # ss://base64...
            myData = Base64Encoder.decode(data[5:]).decode()
            myJSON = XrayCoreConfiguration.build(
                ProxyOutboundObjectSS(*re.split(r'[@:]', myData))
            )

            APP().MainWidget.importServer(
                'sslegacy',
                ujson.dumps(
                    myJSON, indent=2, ensure_ascii=False, escape_forward_slashes=False
                ),
            )

            logger.info(
                f'import share link from clipboard success. '
                f'Remark: sslegacy. Protocol: {Protocol.Shadowsocks}'
            )

            return 'sslegacy', True
        except Exception:
            # Any non-exit exceptions

            return self.parseShareLinkSIP002(data)

    def parseShareLink(self, shareLink):
        try:
            myHead, myBody = shareLink.split('://')
        except Exception:
            # Any non-exit exceptions

            return '', False
        else:
            if myHead.lower() == 'vmess':
                try:
                    myData = Base64Encoder.decode(myBody).decode()
                    myJSON = Configuration.toJSON(myData)
                except Exception:
                    # Any non-exit exceptions

                    return self.parseShareLinkVMess(shareLink, isV2rayN=False)
                else:
                    return self.parseShareLinkVMess(myJSON, isV2rayN=True)

            if myHead.lower() == 'vless':
                return self.parseShareLinkStandard('vless', shareLink)

            if myHead.lower() == 'ss':
                return self.parseShareLinkSS(shareLink)

            return '', False

    def triggeredCallback(self, checked):
        self.clipboard = QApplication.clipboard().text().strip()

        try:
            splitByNewLine = self.clipboard.split('\n')
        except Exception:
            # Any non-exit exceptions

            remark, result = self.parseShareLink(self.clipboard)

            if result:
                # Sync it
                ServerStorage.sync()

                self.showLinkImportOK(remark)
            else:
                self.showLinkErrorBox()
        else:
            successRemark = []

            rowCount = APP().MainWidget.rowCount

            for shareLink in splitByNewLine:
                remark, result = self.parseShareLink(shareLink)

                if result:
                    successRemark.append(remark)

            if len(successRemark) == 0:
                self.showLinkErrorBox()

                return

            # At least one server's been imported. Sync it
            ServerStorage.sync()

            if len(successRemark) == 1:
                # Fall back to single

                self.showLinkImportOK(successRemark[0])
            else:
                importLinkResult = ImportLinkResultBox(successRemark, rowCount)

                # Show the MessageBox and wait for user to close it
                importLinkResult.exec()


class ImportJSONAction(Action):
    def __init__(self, **kwargs):
        super().__init__(_('Import JSON Configuration From Clipboard'), **kwargs)

        self.clipboard = ''

        self.jsonErrorBox = ImportErrorBox(icon=MessageBox.Icon.Critical)
        self.jsonImportOK = JSONImportOKBox(icon=MessageBox.Icon.Information)

    def showJSONErrorBox(self):
        self.jsonErrorBox.setWindowTitle(_('Import'))

        if len(self.clipboard) > 1000:
            self.jsonErrorBox.setText(_('Invalid JSON data.'))
            self.jsonErrorBox.setInformativeText('')
        else:
            self.jsonErrorBox.setText(
                _('Invalid JSON data. The content of the clipboard is:')
            )
            self.jsonErrorBox.setInformativeText(self.clipboard)

        # Show the MessageBox and wait for user to close it
        self.jsonErrorBox.exec()

    def showJSONImportOK(self):
        # Show the MessageBox and wait for user to close it
        choice = self.jsonImportOK.exec()

        if choice == MessageBox.ButtonRole.AcceptRole.value:
            # Go to edit
            APP().MainWidget.show()
        else:
            # OK. Do nothing
            pass

    def triggeredCallback(self, checked):
        self.clipboard = QApplication.clipboard().text().strip()

        try:
            myJSON = Configuration.toJSON(self.clipboard)
        except Exception:
            # Any non-exit exceptions

            self.showJSONErrorBox()
        else:
            APP().MainWidget.importServer(
                _('Untitled'), self.clipboard, syncStorage=True
            )

            logger.info('import JSON configuration from clipboard success')

            self.showJSONImportOK()


class ImportAction(Action):
    def __init__(self):
        super().__init__(
            _('Import'),
            icon=bootstrapIcon('lightning-charge.svg'),
            menu=Menu(
                ImportLinkAction(),
                ImportJSONAction(),
            ),
            useActionGroup=False,
            checkable=True,
        )
