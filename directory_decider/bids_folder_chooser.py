from PyQt5.QtWidgets import *


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
        self.bttn_next = QPushButton('next')
        # TODO smaller browse button under the title
        self.bttn_browse = QPushButton('browse')
        self.layout.addWidget(self.bttn_browse, 2, 0)
        self.layout.addWidget(self.bttn_next, 3, 0)
        self.bttn_browse.clicked.connect(self.open_folder)

    def open_folder(self):
        kwargs = {'caption': 'Select Directory'}
        self.bids_main_dir = str(QFileDialog.getExistingDirectory(**kwargs))
        # TODO validate bids main folder contain key file
        # TODO add key file parser
        self.dir_label.setText(self.bids_main_dir)
