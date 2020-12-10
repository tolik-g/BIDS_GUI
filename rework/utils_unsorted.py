from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal as Signal
import os


class ProjectSubjectSelect(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.project_value = QLineEdit()
        self.subject_value = QLineEdit()

        self.subject_completion()
        self.setup_ui()

    def subject_completion(self):
        names_path = os.path.dirname(os.path.abspath(__file__))
        names_path = os.path.join(names_path, 'random_names.txt')
        print(names_path)
        subjects_ls = ['']

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
        row += 1


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