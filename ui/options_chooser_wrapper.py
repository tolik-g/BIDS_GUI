from PyQt5.QtWidgets import *


class OptionsChooserWrapper(QFrame):
    def __init__(self):
        super().__init__()
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()

        # populate layout
        self.layout_main.addStretch()
        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addStretch()
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # center layout setup
        self.bttn_file = QPushButton('File')
        self.bttn_file.setFixedSize(200, 200)
        self.bttn_folder = QPushButton('Folder')
        self.bttn_folder.setFixedSize(200, 200)
        self.layout_center.addWidget(self.bttn_file, 1, 1)
        self.layout_center.addWidget(self.bttn_folder, 1, 2)

        # navigation layout setup
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
