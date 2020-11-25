from PyQt5.QtWidgets import *

from utils.bids_options import BidsOptions
from utils.ui_utils import create_drop_down_option


class OptionsChooserWrapper(QFrame):
    def __init__(self):
        super().__init__()
        # TODO center and enlarge file and folder buttons
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()

        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # center layout setup
        self.layout_center.setRowStretch(0, 1)
        self.layout_center.setRowStretch(4, 1)
        self.layout_center.setColumnStretch(0, 1)
        self.layout_center.setColumnStretch(1, 1)
        self.layout_center.setColumnStretch(4, 1)
        self.layout_center.setColumnStretch(5, 1)

        # center layout setup
        self.bttn_file = QPushButton('File')
        self.bttn_folder = QPushButton('Folder')
        self.layout_center.addWidget(self.bttn_file, 0, 0)
        self.layout_center.addWidget(self.bttn_folder, 0, 2)

        # navigation layout setup
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
