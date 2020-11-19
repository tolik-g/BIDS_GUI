from PyQt5.QtWidgets import *


class SubjMapping(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        title = QLabel('Please enter the subject name')
        self.layout.addWidget(title, 0, 0)

        # inputs
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('First name')
        self.layout.addWidget(self.name_edit, 1, 1)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText('Last name')
        self.layout.addWidget(self.last_name_edit, 2, 1)

        # buttons
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout.addWidget(self.bttn_next, 3, 1)
        self.layout.addWidget(self.bttn_back, 3, 0)
