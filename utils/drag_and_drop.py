from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QColor
import os
from PyQt5.QtCore import pyqtSignal as Signal
from utils.ui_utils import HLine



class DragDropArea(QFrame):
    dropped = Signal(str)

    def __init__(self, title: str):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameStyle(2)
        self.setMinimumHeight(150)
        self.path = ''

        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_icon = QGridLayout()
        self.layout_or_separate = QGridLayout()
        self.layout_bttn = QGridLayout()

        self.setLayout(self.layout_main)
        self.layout_main.addLayout(self.layout_icon)
        self.layout_main.addLayout(self.layout_or_separate)
        self.layout_main.addLayout(self.layout_bttn)

        # first row icon and caption
        icon = QLabel()
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '../icons/add.png')
        icon.setPixmap(QPixmap(icon_path))
        title = QLabel('Drag & drop your %s here' % title)
        self.layout_icon.addWidget(title, 0, 1)
        self.layout_icon.addWidget(icon, 0, 2)

        self.layout_icon.setColumnStretch(0, 1)
        self.layout_icon.setColumnStretch(3, 1)

        # second row, horizontal lines and "OR" caption
        self.layout_or_separate.addWidget(HLine(), 0, 0)
        self.layout_or_separate.addWidget(QLabel('OR'), 0, 1)
        self.layout_or_separate.addWidget(HLine(), 0, 2)
        self.layout_or_separate.setColumnStretch(0, 1)
        self.layout_or_separate.setColumnStretch(2, 1)

        # browse, upload button
        button_text = 'browse'
        if title == 'folder':
            button_text = 'upload'
        self.bttn = QPushButton(button_text)
        self.layout_bttn.addWidget(self.bttn, 0, 1)
        self.layout_bttn.setColumnStretch(0, 1)
        self.layout_bttn.setColumnStretch(2, 1)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        if not data.hasUrls():
            event.ignore()
        else:
            event.accept()

    def dropEvent(self, event):
        url = event.mimeData().text()[7:]
        self.dropped.emit(url)
