from PyQt5.QtWidgets import *

from ui.options_chooser_file import OptionsChooserFile
from ui.options_chooser_folder import OptionsChooserFolder
from utils.bids_key_file import BidsKeyFile
from utils.bids_options import BidsOptions
from utils.bids_options_file import BidsOptionsFile
from utils.bids_options_folder import BidsOptionsFolder
from utils.bids_subject import BidsSubject
from utils.ui_utils import show_warn_message
from ui.folder_chooser import FolderChooser
from ui.options_chooser_wrapper import OptionsChooserWrapper
from ui.subject_chooser import SubjectChooser


class Manager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bids_subject = BidsSubject()
        self.bids_key_file = BidsKeyFile()
        self.bids_options_chooser = None
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
        widget.bttn_next.clicked.connect(self.show_options_chooser_wrapper)
        widget.bttn_back.clicked.connect(self.show_bids_folder_chooser)
        self.layout.addWidget(widget)

    def show_options_chooser_wrapper(self):
        if not self.subject_validate():
            return
        self.clear_layout()
        widget = OptionsChooserWrapper()
        widget.bttn_folder.clicked.connect(lambda: self.show_options_chooser(BidsOptions.Type.FOLDER))
        widget.bttn_file.clicked.connect(lambda: self.show_options_chooser(BidsOptions.Type.FILE))
        widget.bttn_back.clicked.connect(self.show_subj_chooser)
        self.layout.addWidget(widget)

    def show_options_chooser(self, option_type: BidsOptions.Type):
        self.clear_layout()
        if option_type == BidsOptions.Type.FILE:
            self.bids_options_chooser = BidsOptionsFile()
            widget = OptionsChooserFile(self.bids_options_chooser)
        else:
            self.bids_options_chooser = BidsOptionsFolder()
            widget = OptionsChooserFolder(self.bids_options_chooser)

        widget.bttn_next.clicked.connect(self.start_over)
        widget.bttn_back.clicked.connect(self.show_options_chooser_wrapper)
        self.layout.addWidget(widget)

    def start_over(self):
        print('done -> display the user a button to start over?')
        print(self.bids_options_chooser.selected)

    def subject_validate(self):
        if not self.bids_subject.validate_empty():
            show_warn_message("Oops", "Please fill the subject full name")
            return False
        print('subject key folder:' +
              self.bids_key_file.subject_to_key(self.bids_subject))
        return True
