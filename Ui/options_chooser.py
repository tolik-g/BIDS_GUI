from PyQt5.QtWidgets import *


class OptionsChooser(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # TODO: placeholder widget, delete later
        placeholder = QLabel('Choose options')
        self.layout.addWidget(placeholder, 0, 0)

        # buttons
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout.addWidget(self.bttn_next, 1, 1)
        self.layout.addWidget(self.bttn_back, 1, 0)
