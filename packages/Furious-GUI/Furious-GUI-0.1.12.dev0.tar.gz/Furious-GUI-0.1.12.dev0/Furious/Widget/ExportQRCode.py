from Furious.Utility.Constants import APPLICATION_NAME
from Furious.Utility.Utility import SupportConnectedCallback, bootstrapIcon
from Furious.Utility.Translator import gettext as _

from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget

import io
import pyqrcode


class ExportQRCode(SupportConnectedCallback, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(_(APPLICATION_NAME))
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-window.svg'))

        self.labelList = []

        self.editorTab = QTabWidget(self)
        self.editorTab.setTabsClosable(True)
        self.editorTab.tabCloseRequested.connect(self.handleTabCloseRequested)

        self.setCentralWidget(self.editorTab)

    def initTabWithData(self, data):
        for text, link in data:
            qrdata = io.BytesIO()

            qrcode = pyqrcode.create(link)
            qrcode.png(qrdata, scale=5)

            pixmap = QPixmap()
            pixmap.loadFromData(qrdata.getvalue(), 'PNG')

            label = QLabel(parent=self.editorTab)
            label.setPixmap(pixmap)

            self.labelList.append(label)
            self.editorTab.addTab(label, text)

    @QtCore.Slot(int)
    def handleTabCloseRequested(self, index):
        self.editorTab.removeTab(index)

        if self.editorTab.count() == 0:
            self.hide()

    def connectedCallback(self):
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-connected-dark.svg'))

    def disconnectedCallback(self):
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-window.svg'))
