from PyQt5.QtWidgets import *

from directory_decider.bids_folder_chooser import BidsFolderChooser
from directory_decider.folder_mapping import FolderMapping
from directory_decider.subj_mapping import SubjMapping


class DirectoryDecider(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        widget = SubjMapping()
        widget.bttn_next.clicked.connect(self.show_folder_mapping)
        widget.bttn_back.clicked.connect(self.show_bids_folder_chooser)
        self.layout.addWidget(widget)

    def show_folder_mapping(self):
        self.clear_layout()
        widget = FolderMapping()
        widget.bttn_next.clicked.connect(lambda: print('done'))
        widget.bttn_back.clicked.connect(self.show_subj_mapping)
        self.layout.addWidget(widget)

