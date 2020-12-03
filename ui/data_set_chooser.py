from PyQt5.QtWidgets import *
import os.path

from data.bids_key_file import BidsKeyFile
from data.bids_options_factory import BidsOptionsFactory
from utils.common import show_warn_message


class DataSetChooser(QFrame):
    BIDS_KEY_FILE = "BIDS_KEYS.csv"

    def __init__(self, key_file: BidsKeyFile, factory: BidsOptionsFactory):
        super().__init__()
        self.bids_dataset_dir = None
        self.key_file = key_file
        self.options_factory = factory

        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_browse = QGridLayout()
        self.layout_title = QGridLayout()
        self.setLayout(self.layout_main)
        self.layout_main.addLayout(self.layout_browse)
        self.layout_main.addLayout(self.layout_navigation_bttns)

        # title layout setup
        title = QLabel('Choose Data set folder')
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
        self.bids_dataset_dir = str(QFileDialog.getExistingDirectory(**kwargs))
        self.dir_label.setText(self.bids_dataset_dir)
        self.validate_data_set_folder()

    def validate_data_set_folder(self):
        folder_name = os.path.basename(self.bids_dataset_dir)
        if folder_name not in BidsOptionsFactory.DATASETS:
            self.show_warn('Invalid data set folder: ' + folder_name)
            return

        root_folder = os.path.abspath(os.path.join(self.bids_dataset_dir, os.pardir))
        file = os.path.join(root_folder, DataSetChooser.BIDS_KEY_FILE)
        if os.path.isfile(file):
            self.bttn_next.setEnabled(True)
            self.key_file.set_file(file)
            self.options_factory.set_data_set(folder_name)
        else:
            self.show_warn("Bids key file is missing from root folder")

    def show_warn(self, msg: str):
        self.bttn_next.setEnabled(False)
        show_warn_message("Oops", msg)
