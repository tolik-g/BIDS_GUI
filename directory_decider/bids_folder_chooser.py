from PyQt5.QtWidgets import *


class BidsFolderChooser(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # TODO: placeholder widget, delete later
        placeholder = QLabel('bids folder chooser')
        self.layout.addWidget(placeholder, 0, 0)

        # buttons
        self.bttn_next = QPushButton('next')
        self.layout.addWidget(self.bttn_next, 1, 0)
