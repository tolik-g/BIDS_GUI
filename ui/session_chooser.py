from PyQt5.QtWidgets import *


class SessionChooser(QWidget):
    def __init__(self, *args, session_ls, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.session_ls = session_ls
        self.session_dropdown = QComboBox()
        self.session_dropdown.addItems(session_ls)

        # layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(QLabel('Choose Session'))
        self.layout.addWidget(self.session_dropdown)
