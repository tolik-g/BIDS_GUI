from PyQt5.QtWidgets import *


class SubjectChooser(QFrame):
    def __init__(self, modify_cb, state):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        title = QLabel('Please enter the subject name')
        self.layout.addWidget(title, 0, 0)

        # inputs
        self.name_edit = QLineEdit(state['subject_name'])
        self.name_edit.setPlaceholderText('First name')
        self.name_edit.textChanged.connect(lambda: modify_cb(self.get_subject()))
        self.layout.addWidget(self.name_edit, 1, 1)

        self.last_name_edit = QLineEdit(state['subject_last_name'])
        self.last_name_edit.setPlaceholderText('Last name')
        self.last_name_edit.textChanged.connect(lambda: modify_cb(self.get_subject()))
        self.layout.addWidget(self.last_name_edit, 2, 1)

        # buttons
        self.bttn_next = QPushButton('next')
        self.bttn_back = QPushButton('back')
        self.layout.addWidget(self.bttn_next, 3, 1)
        self.layout.addWidget(self.bttn_back, 3, 0)

    def get_subject(self):
        return self.name_edit.text(), self.last_name_edit.text()
