import ntpath

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import pyqtSignal as Signal


class DragDropArea(QFrame):
    path_modified = Signal(str)

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setFrameStyle(2)
        self.setMinimumHeight(150)
        self.setMinimumWidth(300)
        self.path = ''

        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_icon = QGridLayout()

        self.setLayout(self.layout_main)
        self.layout_main.addLayout(self.layout_icon)

        # first row icon and caption
        icon = QLabel()
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '../assets/add.png')
        icon.setPixmap(QPixmap(icon_path))
        title = QLabel('Drag & drop your file / folder here')
        self.path_label = QLabel('')

        self.layout_icon.addWidget(title, 0, 1)
        self.layout_icon.addWidget(icon, 0, 2)
        self.layout_icon.addWidget(self.path_label, 1, 1)

        self.layout_icon.setColumnStretch(0, 1)
        self.layout_icon.setColumnStretch(3, 1)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        event.ignore() if not data.hasUrls() else event.accept()

    def dropEvent(self, event):
        url = event.mimeData().text()[8:]
        self.path_modified.emit(url)
        self.path_label.setText(ntpath.basename(url))
