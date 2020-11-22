from PyQt5.QtWidgets import *

from Utils.bids_key_file import BidsKeyFile
from Utils.bids_options import BidsOptions
from Utils.bids_subject import BidsSubject
from Utils.ui_utils import show_warn_message
from Ui.folder_chooser import FolderChooser
from Ui.options_chooser import OptionsChooser
from Ui.subject_chooser import SubjectChooser


class Manager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bids_subject = BidsSubject()
        self.bids_key_file = BidsKeyFile()
        self.bids_options_chooser = BidsOptions()
        self.show_bids_folder_chooser()

    def clear_layout(self):
        for i in range(self.layout.count())[::-1]:
            item = self.layout.takeAt(i)
            item.widget().deleteLater()

    def show_bids_folder_chooser(self):
        self.clear_layout()
        widget = FolderChooser(self.bids_key_file)
        widget.bttn_next.clicked.connect(self.show_subj_chooser)
        self.layout.addWidget(widget)

    def show_subj_chooser(self):
        self.clear_layout()
        widget = SubjectChooser(self.bids_subject)
        widget.bttn_next.clicked.connect(self.show_options_chooser)
        widget.bttn_back.clicked.connect(self.show_bids_folder_chooser)
        self.layout.addWidget(widget)

    def show_options_chooser(self):
        if not self.subject_validate():
            return
        self.clear_layout()
        widget = OptionsChooser(self.bids_options_chooser)
        widget.bttn_next.clicked.connect(lambda: print('done'))
        widget.bttn_back.clicked.connect(self.show_subj_chooser)
        self.layout.addWidget(widget)

    def subject_validate(self):
        if not self.bids_subject.validate_empty():
            show_warn_message("Oops", "Please fill the subject full name")
            return False
        print('subject key folder:' + self.bids_key_file.subject_to_key(self.bids_subject))
        return True
