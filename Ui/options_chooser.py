from PyQt5.QtWidgets import *

from Utils.bids_options import BidsOptions
from Utils.ui_utils import create_drop_down_option


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # TODO: placeholder widget, delete later
        placeholder = QLabel('Choose options')
        self.layout.addWidget(placeholder, 0, 0)

        label1, dropdown1 = create_drop_down_option(BidsOptions.OPTION_A, options)
        label2, dropdown2 = create_drop_down_option(BidsOptions.OPTION_B, options)

        self.layout.addWidget(label1, 1, 0)
        self.layout.addWidget(dropdown1, 1, 1, 1, 4)

        self.layout.addWidget(label2, 2, 0)
        self.layout.addWidget(dropdown2, 2, 1, 1, 4)

        # buttons
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout.addWidget(self.bttn_next, 3, 1)
        self.layout.addWidget(self.bttn_back, 3, 0)
