from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal as Signal
import os

icons_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = os.path.split(icons_dir)[0]
print(icons_dir)
VALID_ICON_PATH = os.path.join(icons_dir, 'icons/valid.png')
INVALID_ICON_PATH = os.path.join(icons_dir, 'icons/invalid.png')


class ProjectSubjectSelect(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.project_value = QLineEdit()
        self.subject_value = QLineEdit()
        self.subject_ls = None
        self.subject_icon = QLabel()

        # signals
        self.subject_changed = self.subject_value.textEdited

        self.set_valid_subject(False)
        self.setup_ui()

    def update_subject_list(self, subject_ls):
        self.subject_ls = subject_ls
        completer = QCompleter(subject_ls)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.subject_value.setCompleter(completer)

    def setup_ui(self):
        row = 0

        # project
        project_label = QLabel('Project')
        self.layout.addWidget(project_label, row, 0)
        self.layout.addWidget(self.project_value, row, 1)
        row += 1

        # subject
        subject_label = QLabel('Subject')
        self.layout.addWidget(subject_label, row, 0)
        self.layout.addWidget(self.subject_value, row, 1)
        self.layout.addWidget(self.subject_icon, row, 2)
        row += 1

    def set_valid_subject(self, toggle: bool):
        if toggle:
            self.subject_icon.setPixmap(QPixmap(VALID_ICON_PATH))
        else:
            self.subject_icon.setPixmap(QPixmap(INVALID_ICON_PATH))
            print(INVALID_ICON_PATH)


class SaveButton(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.save_bttn = QPushButton('save')
        self.clicked = self.save_bttn.clicked

        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.save_bttn)
        self.layout.addStretch()

    def toggle(self, toggle: bool):
        self.save_bttn.setEnabled(toggle)


class HLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)


class VLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)