from PyQt5.QtWidgets import *

from utils.bids_subject import BidsSubject


class SubjectChooser(QFrame):
    def __init__(self, subject: BidsSubject):
        super().__init__()
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_name = QGridLayout()
        self.layout_title = QGridLayout()

        self.setLayout(self.layout_main)
        self.layout_main.addLayout(self.layout_name)
        self.layout_main.addLayout(self.layout_navigation_bttns)

        # title layout setup
        title = QLabel("Enter the subject's name")
        title.setObjectName('title')
        self.layout_title.setColumnStretch(0, 1)
        self.layout_title.setColumnStretch(2, 1)
        self.layout_title.addWidget(title, 0, 1)

        # names layout setup
        self.name_edit = QLineEdit(subject.get_first_name())
        self.name_edit.setPlaceholderText('First name')
        self.name_edit.textChanged.connect(
            lambda: subject.set_first_name(self.name_edit.text()))
        self.last_name_edit = QLineEdit(subject.get_last_name())
        self.last_name_edit.setPlaceholderText('Last name')
        self.last_name_edit.textChanged.connect(
            lambda: subject.set_last_name(self.last_name_edit.text()))

        self.layout_name.setColumnStretch(0, 1)
        self.layout_name.setColumnStretch(2, 1)
        self.layout_name.setRowStretch(0, 1)
        self.layout_name.setRowStretch(4, 1)
        self.layout_name.addLayout(self.layout_title, 1, 1)
        self.layout_name.addWidget(self.name_edit, 2, 1)
        self.layout_name.addWidget(self.last_name_edit, 3, 1)

        # navigation layout setup
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
        self.layout_navigation_bttns.addWidget(self.bttn_next, 0, 2)


