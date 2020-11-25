from PyQt5.QtWidgets import *
import os.path

from utils.bids_key_file import BidsKeyFile
from utils.ui_utils import show_warn_message


class FolderChooser(QFrame):
    BIDS_KEY_FILE = "BIDS_KEYS.csv"

    def __init__(self, key_file: BidsKeyFile):
        super().__init__()
        self.bids_main_dir = None
        self.key_file = key_file

        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_browse = QGridLayout()
        self.layout_title = QGridLayout()
        self.setLayout(self.layout_main)
        self.layout_main.addLayout(self.layout_browse)
        self.layout_main.addLayout(self.layout_navigation_bttns)

        # title layout setup
        title = QLabel('Choose main BIDS folder')
        title.setObjectName('title')
        self.layout_title.setColumnStretch(0, 1)
        self.layout_title.setColumnStretch(2, 1)
        self.layout_title.addWidget(title, 0, 1)

        # browse layout setup
        key_path = key_file.get_file()
        self.dir_label = QLineEdit(os.path.dirname(key_path))
        self.dir_label.setReadOnly(True)
        self.dir_label.setFixedWidth(400)
        self.bttn_browse = QPushButton('browse')
        self.bttn_browse.clicked.connect(self.open_folder)
        self.layout_browse.setRowStretch(0, 1)
        self.layout_browse.setRowStretch(3, 1)
        self.layout_browse.setColumnStretch(0, 1)
        self.layout_browse.setColumnStretch(3, 1)
        self.layout_browse.addLayout(self.layout_title, 1, 1, 1, 2)
        self.layout_browse.addWidget(self.bttn_browse, 2, 1)
        self.layout_browse.addWidget(self.dir_label, 2, 2)

        # navigation layout setup
        self.bttn_next = QPushButton('next')
        self.layout_navigation_bttns.setColumnStretch(0, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_next, 0, 1)
        # self.bttn_next.setEnabled(key_path != '')

    def open_folder(self):
        kwargs = {'caption': 'Select Directory'}
        self.bids_main_dir = str(QFileDialog.getExistingDirectory(**kwargs))
        self.dir_label.setText(self.bids_main_dir)
        self.validate_key_file_exist()

    def validate_key_file_exist(self):
        file = os.path.join(self.bids_main_dir, FolderChooser.BIDS_KEY_FILE)
        if os.path.isfile(file):
            self.bttn_next.setEnabled(True)
            self.key_file.set_file(file)
        else:
            self.bttn_next.setEnabled(False)
            show_warn_message("Oops", "Folder does not contain bids key file")
