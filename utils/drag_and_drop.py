from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import pyqtSignal as Signal


class DragDropArea(QFrame):
    dropped = Signal(str)

    def __init__(self, title: str):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameStyle(2)
        self.layout = QGridLayout()
        self.setMinimumHeight(150)

        icon = QLabel()
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '../icons/add.png')
        icon.setPixmap(QPixmap(icon_path))

        title = QLabel('Drag & drop your %s here' % title)

        self.layout.addWidget(title, 1, 1)
        self.layout.addWidget(icon, 1, 2)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(2, 1)
        self.setLayout(self.layout)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        if not data.hasUrls():
            print('no urls')
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        url = event.mimeData().text()[7:]
        self.dropped.emit(url)
