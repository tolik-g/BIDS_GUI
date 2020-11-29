from PyQt5.QtWidgets import *

from ui.options_chooser import OptionsChooser
from data.bids_key_file import BidsKeyFile
from data.bids_options import BidsOptions
from data.bids_options_file import BidsOptionsFile
from data.bids_options_folder import BidsOptionsFolder
from data.bids_subject import BidsSubject
from utils.common import show_warn_message
from ui.key_file_chooser import KeyFileChooser
from ui.options_chooser_wrapper import OptionsChooserWrapper
from ui.subject_chooser import SubjectChooser
from utils.subject_status import SubjectStatus


class Manager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bids_subject = BidsSubject()
        self.bids_key_file = BidsKeyFile()
        self.bids_options_chooser = BidsOptions()
        self.show_bids_folder_chooser()
        self.is_new_subject = None

    def clear_layout(self):
        for i in range(self.layout.count())[::-1]:
            item = self.layout.takeAt(i)
            item.widget().deleteLater()

    def show_bids_folder_chooser(self):
        self.clear_layout()
        widget = KeyFileChooser(self.bids_key_file)
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
        self.bids_options_chooser = BidsOptionsFile() if option_type == BidsOptions.Type.FILE else BidsOptionsFolder()

        subject_status_widget = SubjectStatus(first_name=self.bids_subject.get_first_name(),
                                              last_name=self.bids_subject.get_last_name(),
                                              subject_key=self.get_current_subject_key())
        widget = OptionsChooser(self.bids_options_chooser,
                                subject_status=subject_status_widget)
        widget.bttn_finish.clicked.connect(self.finish)
        widget.bttn_back.clicked.connect(self.show_options_chooser_wrapper)
        self.layout.addWidget(widget)

    def finish(self):
        print('done -> display the user a button to start over?')
        print(self.bids_options_chooser.selected)
        print('is valid: ' + str(self.bids_options_chooser.is_single_option_selected()))

        if self.is_new_subject:
            print('saving changes to key file!')
            self.is_new_subject = False
            self.bids_key_file.create_new_key(self.bids_subject.get_full_name())

    def subject_validate(self):
        if not self.bids_subject.validate_empty():
            show_warn_message("Oops", "Please fill the subject full name")
            return False
        return True

    def get_current_subject_key(self):
        subject_key = self.bids_key_file.subject_to_key(
            self.bids_subject.get_full_name())
        if subject_key == '':
            self.is_new_subject = True
            subject_key = self.bids_key_file.find_new_key()
        else:
            self.is_new_subject = False
        return subject_key
