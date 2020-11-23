from PyQt5.QtWidgets import *

from utils.bids_options import BidsOptions
from utils.ui_utils import create_drop_down_option


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions):
        super().__init__()
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()
        self.layout_title = QGridLayout()
        self.layout_browse = QGridLayout()
        self.layout_dropdown = QGridLayout()

        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # title layout setup
        title = QLabel('Choose options')
        title.setObjectName('title')
        self.layout_title.setColumnStretch(0, 1)
        self.layout_title.setColumnStretch(2, 1)
        self.layout_title.addWidget(title, 0, 1)

        # browse layout setup
        self.dir_label = QLineEdit()
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

        # dropdown layout setup
        label1, dropdown1 = create_drop_down_option(BidsOptions.OPTION_A,
                                                    options)
        label2, dropdown2 = create_drop_down_option(BidsOptions.OPTION_B,
                                                    options)
        self.layout_dropdown.addWidget(label1, 0, 0)
        self.layout_dropdown.addWidget(dropdown1, 0, 1)
        self.layout_dropdown.addWidget(label2, 1, 0)
        self.layout_dropdown.addWidget(dropdown2, 1, 1)

        # center layout setup
        self.layout_center.setRowStretch(0, 1)
        self.layout_center.setRowStretch(4, 1)
        self.layout_center.setColumnStretch(0, 1)
        self.layout_center.setColumnStretch(1, 1)
        self.layout_center.setColumnStretch(4, 1)
        self.layout_center.setColumnStretch(5, 1)
        self.layout_center.addLayout(self.layout_browse, 1, 1, 1, 4)
        self.layout_center.addLayout(self.layout_dropdown, 2, 2, 1, 2)

        # navigation layout setup
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
        self.layout_navigation_bttns.addWidget(self.bttn_next, 0, 2)

    def open_folder(self):
        kwargs = {'caption': 'Select Directory'}
        path = str(QFileDialog.getExistingDirectory(**kwargs))
        if path == '':
            return
        self.dir_label.setText(path)
