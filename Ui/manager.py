from PyQt5.QtWidgets import *

from Utils.bids_key_file import BidsKeyFile
from Utils.bids_subject import BidsSubject
from Utils.ui_utils import show_warn_message
from Ui.bids_folder_chooser import BidsFolderChooser
from Ui.folder_mapping import FolderMapping
from Ui.subject_chooser import SubjectChooser


class Manager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bids_subject = BidsSubject()
        self.bids_key_file = BidsKeyFile()
        self.show_bids_folder_chooser()

    def clear_layout(self):
        for i in range(self.layout.count())[::-1]:
            item = self.layout.takeAt(i)
            item.widget().deleteLater()

    def show_bids_folder_chooser(self):
        self.clear_layout()
        widget = BidsFolderChooser(self.bids_key_file)
        widget.bttn_next.clicked.connect(self.show_subj_mapping)
        self.layout.addWidget(widget)

    def show_subj_mapping(self):
        self.clear_layout()
        widget = SubjectChooser(self.bids_subject)
        widget.bttn_next.clicked.connect(self.show_folder_mapping)
        widget.bttn_back.clicked.connect(self.show_bids_folder_chooser)
        self.layout.addWidget(widget)

    def show_folder_mapping(self):
        if not self.subject_validate():
            return
        self.clear_layout()
        widget = FolderMapping()
        widget.bttn_next.clicked.connect(lambda: print('done'))
        widget.bttn_back.clicked.connect(self.show_subj_mapping)
        self.layout.addWidget(widget)

    def subject_validate(self):
        if not self.bids_subject.validate_empty():
            show_warn_message("Oops", "Please fill the subject full name")
            return False
        # TODO use bids key file utils here to get subject mapping and fill data with it
        return True
