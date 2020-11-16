from PyQt5.QtWidgets import *


class FolderMapping(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # TODO: placeholder widget, delete later
        placeholder = QLabel('Folder mapping screen')
        self.layout.addWidget(placeholder, 0, 0)

        # next screen button
        self.bttn_next = QPushButton('next')
        self.layout.addWidget(self.bttn_next, 1, 0)
