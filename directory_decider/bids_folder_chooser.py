from PyQt5.QtWidgets import *
import os.path

from Utils.ui_utils import show_warn_message

BIDS_KEY_FILE = "BIDS_KEYS.csv"


class BidsFolderChooser(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.bids_main_dir = None
        self.dir_label = None

        # TODO center the title label
        title = QLabel('Choose main BIDS folder')
        self.dir_label = QLabel('')
        self.layout.addWidget(title, 0, 0)
        self.layout.addWidget(self.dir_label, 1, 0)

        # buttons
        # TODO smaller browse button under the title
        self.bttn_next = QPushButton('next')
        self.bttn_browse = QPushButton('browse')
        self.layout.addWidget(self.bttn_browse, 2, 0)
        self.layout.addWidget(self.bttn_next, 3, 0)
        self.bttn_browse.clicked.connect(self.open_folder)
        self.bttn_next.setEnabled(False)

    def open_folder(self):
        kwargs = {'caption': 'Select Directory'}
        self.bids_main_dir = str(QFileDialog.getExistingDirectory(**kwargs))
        self.dir_label.setText(self.bids_main_dir)
        self.validate_key_file_exist()

    def validate_key_file_exist(self):
        file = os.path.join(self.bids_main_dir, BIDS_KEY_FILE)
        if os.path.isfile(file):
            self.bttn_next.setEnabled(True)
        else:
            self.bttn_next.setEnabled(False)
            show_warn_message("Error", "Folder does not contain bids key file")
