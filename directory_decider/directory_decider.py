from PyQt5.QtWidgets import *
from directory_decider.folder_mapping import FolderMapping
from directory_decider.subj_mapping import SubjMapping


class DirectoryDecider(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.advance_subj_mapping()

    def clear_layout(self):
        for i in range(self.layout.count())[::-1]:
            item = self.layout.takeAt(i)
            item.widget().deleteLater()

    def advance_subj_mapping(self):
        self.clear_layout()
        widget = SubjMapping()
        widget.bttn_next.clicked.connect(self.advance_folder_mapping)
        self.layout.addWidget(widget)

    def advance_folder_mapping(self):
        self.clear_layout()
        widget = FolderMapping()
        widget.bttn_next.clicked.connect(self.clear_layout)
        self.layout.addWidget(widget)

