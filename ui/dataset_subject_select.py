from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import os

# find relative path to assets
icons_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = os.path.split(icons_dir)[0]

# constants
VALID_ICON_PATH = os.path.join(icons_dir, 'assets/valid.png')
INVALID_ICON_PATH = os.path.join(icons_dir, 'assets/invalid.png')


class ProjectSubjectSelect(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.dataset_value = QComboBox()
        self.subject_value = QLineEdit()
        self.subject_ls = None
        self.subject_icon = QLabel()

        # signals
        # signal emitted when subject text is changed
        self.subject_changed = self.subject_value.textEdited

        # generic widget setup
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def update_subject_list(self, subject_ls: list):
        """
        add auto completion to subject input
        :param subject_ls: list of subject names
        :return:
        """
        self.subject_ls = subject_ls
        completer = QCompleter(subject_ls)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.subject_value.setCompleter(completer)

    def update_dataset_list(self, dataset_ls: list):
        """
        update list of datasets available
        :param dataset_ls:
        :return:
        """
        self.dataset_value.clear()
        self.dataset_value.addItems(dataset_ls)

    def setup_ui(self):
        # start with "invalid" icon for subject
        self.set_valid_subject(False)

        row = 0

        # project
        dataset_label = QLabel('Dataset')
        self.layout.addWidget(dataset_label, row, 0)
        self.layout.addWidget(self.dataset_value, row, 1)
        row += 1

        # subject
        subject_label = QLabel('Subject')
        self.layout.addWidget(subject_label, row, 0)
        self.layout.addWidget(self.subject_value, row, 1)
        self.layout.addWidget(self.subject_icon, row, 2)
        row += 1

    def set_valid_subject(self, toggle: bool):
        """
        set valid/invalid subject icon
        :param toggle: True = valid, False = invalid
        :return:
        """
        if toggle:
            self.subject_icon.setPixmap(QPixmap(VALID_ICON_PATH))
        else:
            self.subject_icon.setPixmap(QPixmap(INVALID_ICON_PATH))
