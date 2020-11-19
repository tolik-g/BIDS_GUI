from PyQt5.QtWidgets import *

from Utils.ui_utils import show_warn_message
from directory_decider.bids_folder_chooser import BidsFolderChooser
from directory_decider.folder_mapping import FolderMapping
from directory_decider.subject_chooser import SubjectChooser


class DirectoryDecider(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {'subject_name': '', 'subject_last_name': ''}
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.show_bids_folder_chooser()

    def clear_layout(self):
        for i in range(self.layout.count())[::-1]:
            item = self.layout.takeAt(i)
            item.widget().deleteLater()

    def show_bids_folder_chooser(self):
        self.clear_layout()
        widget = BidsFolderChooser()
        widget.bttn_next.clicked.connect(self.show_subj_mapping)
        self.layout.addWidget(widget)

    def show_subj_mapping(self):
        self.clear_layout()
        widget = SubjectChooser(self.subject_modified, self.data)
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

    def subject_modified(self, value):
        self.data['subject_name'] = value[0]
        self.data['subject_last_name'] = value[1]

    def subject_validate(self):
        if self.data['subject_name'] == '' or self.data['subject_last_name'] == '':
            show_warn_message("Oops", "Please fill the subject full name")
            return False
        # TODO use bids key file utils here to get subject mapping and fill data with it
        return True


