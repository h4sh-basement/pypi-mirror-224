from Furious.Gui.Icon import Icon
from Furious.Utility.Constants import APP, PLATFORM, ROOT_DIR

from PySide6.QtWidgets import QApplication

import os
import copy
import ujson
import logging
import pybase64
import functools
import subprocess

logger = logging.getLogger(__name__)


class Base64Encoder:
    @staticmethod
    def encode(text):
        return pybase64.b64encode(text)

    @staticmethod
    def decode(text):
        return pybase64.b64decode(text, validate=False)


class Protocol:
    VMess = 'VMess'
    VLESS = 'VLESS'
    Shadowsocks = 'shadowsocks'
    Hysteria = 'hysteria'


class StateContext:
    def __init__(self, ob, *args, **kwargs):
        super().__init__(*args, **kwargs)

        assert hasattr(ob, 'setDisabled')

        self._ob = ob

    def __enter__(self):
        self._ob.setDisabled(True)

    def __exit__(self, exceptionType, exceptionValue, tb):
        self._ob.setDisabled(False)


class ServerStorage:
    EMPTY_OBJECT = {'model': []}

    @staticmethod
    def init():
        return copy.deepcopy(ServerStorage.EMPTY_OBJECT)

    @staticmethod
    def sync(ob=None):
        if ob is None:
            # Object is up-to-date
            APP().Configuration = ServerStorage.toStorage(APP().MainWidget.StorageObj)
        else:
            # Object is up-to-date
            APP().Configuration = ServerStorage.toStorage(ob)

    @staticmethod
    def toObject(st):
        if not st:
            # Server storage does not exist, or is empty
            return ServerStorage.init()

        return ujson.loads(Base64Encoder.decode(st))

    @staticmethod
    def toStorage(ob):
        return Base64Encoder.encode(
            ujson.dumps(ob, ensure_ascii=False, escape_forward_slashes=False).encode()
        )

    @staticmethod
    def clear():
        APP().Configuration = ''
        APP().ActivatedItemIndex = str(-1)


class RoutesStorage:
    # remark, corename, routes
    EMPTY_OBJECT = {'model': []}

    @staticmethod
    def init():
        return copy.deepcopy(RoutesStorage.EMPTY_OBJECT)

    @staticmethod
    def sync(ob=None):
        if ob is None:
            # Object is up-to-date
            APP().CustomRouting = RoutesStorage.toStorage(
                APP().editRoutingWidget.StorageObj
            )
        else:
            # Object is up-to-date
            APP().CustomRouting = RoutesStorage.toStorage(ob)

    @staticmethod
    def toObject(st):
        if not st:
            # Server storage does not exist, or is empty
            return RoutesStorage.init()

        return ujson.loads(Base64Encoder.decode(st))

    @staticmethod
    def toStorage(ob):
        return Base64Encoder.encode(
            ujson.dumps(ob, ensure_ascii=False, escape_forward_slashes=False).encode()
        )

    @staticmethod
    def clear():
        APP().CustomRouting = ''


class Switch:
    OFF = '0'
    ON_ = '1'

    RANGE = [OFF, ON_]


class SupportConnectedCallback:
    Object = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        SupportConnectedCallback.Object.append(self)

    def disconnectedCallback(self):
        raise NotImplementedError

    def connectedCallback(self):
        raise NotImplementedError

    @staticmethod
    def callConnectedCallback():
        for ob in SupportConnectedCallback.Object:
            assert isinstance(ob, SupportConnectedCallback)

            ob.connectedCallback()

    @staticmethod
    def callDisconnectedCallback():
        for ob in SupportConnectedCallback.Object:
            assert isinstance(ob, SupportConnectedCallback)

            ob.disconnectedCallback()


class SupportThemeChangedCallback:
    Object = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        SupportThemeChangedCallback.Object.append(self)

    def themeChangedCallback(self, theme):
        raise NotImplementedError

    @staticmethod
    def callThemeChangedCallback(theme):
        logger.info(f'system theme changed to {theme}')

        for ob in SupportThemeChangedCallback.Object:
            assert isinstance(ob, SupportThemeChangedCallback)

            ob.themeChangedCallback(theme)


def icon(prefix, name):
    if name.startswith('rocket-takeoff'):
        # Colorful. Use default
        return Icon(f':/Icons/bootstrap/{name}')
    else:
        return Icon(f':/Icons/{prefix}/{name}')


bootstrapIcon = functools.partial(icon, 'bootstrap')
bootstrapIconWhite = functools.partial(icon, 'bootstrap/white')


def protocolRepr(protocol):
    if protocol.lower() == 'vmess':
        return Protocol.VMess

    if protocol.lower() == 'vless':
        return Protocol.VLESS

    if protocol.lower() == 'shadowsocks':
        return Protocol.Shadowsocks

    return protocol


def getAbsolutePath(path):
    return path if os.path.isabs(path) else str(ROOT_DIR / path)


def getUbuntuRelease():
    try:
        result = subprocess.run(
            ['cat', '/etc/lsb-release'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

        values = dict(
            list(line.split('='))
            for line in filter(lambda x: x != '', result.stdout.decode().split('\n'))
        )

        if values['DISTRIB_ID'] == 'Ubuntu':
            return values['DISTRIB_RELEASE']
        else:
            return ''
    except Exception:
        # Any non-exit exceptions

        return ''


def swapListItem(listOrTuple, index0, index1):
    swap = listOrTuple[index0]

    listOrTuple[index0] = listOrTuple[index1]
    listOrTuple[index1] = swap


def moveToCenter(widget, parent=None):
    geometry = widget.geometry()

    if parent is None:
        center = QApplication.primaryScreen().availableGeometry().center()
    else:
        center = parent.geometry().center()

    geometry.moveCenter(center)

    widget.move(geometry.topLeft())
