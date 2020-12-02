from PyQt5.QtWidgets import *

from data_sets.preterm_options_file import PretermOptionsFile
from data_sets.preterm_options_folder import PretermOptionsFolder
from ui.options_chooser import OptionsChooser
from data.bids_key_file import BidsKeyFile
from data.bids_options import BidsOptions
from data.bids_subject import BidsSubject
from data.bids_file import BidsFile
from utils.common import show_warn_message, clear_layout
from ui.key_file_chooser import KeyFileChooser
from ui.options_chooser_wrapper import OptionsChooserWrapper
from ui.subject_chooser import SubjectChooser


class Manager(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.bids_subject = BidsSubject()
        self.bids_key_file = BidsKeyFile()
        self.bids_options_chooser = BidsOptions()
        self.bids_file = BidsFile()
        self.show_bids_folder_chooser()
        self.is_new_subject = None

    def show_bids_folder_chooser(self):
        clear_layout(self.layout)
        widget = KeyFileChooser(self.bids_key_file)
        widget.bttn_next.clicked.connect(self.show_subj_chooser)
        self.layout.addWidget(widget)

    def show_subj_chooser(self):
        clear_layout(self.layout)
        widget = SubjectChooser(self.bids_subject)
        widget.bttn_next.clicked.connect(self.show_options_chooser_wrapper)
        widget.bttn_back.clicked.connect(self.show_bids_folder_chooser)
        self.layout.addWidget(widget)

    def show_options_chooser_wrapper(self):
        if not self.subject_validate():
            return

        clear_layout(self.layout)
        widget = OptionsChooserWrapper()
        widget.bttn_folder.clicked.connect(lambda: self.show_options_chooser(BidsOptions.Type.FOLDER))
        widget.bttn_file.clicked.connect(lambda: self.show_options_chooser(BidsOptions.Type.FILE))
        widget.bttn_back.clicked.connect(self.show_subj_chooser)
        self.layout.addWidget(widget)

    def show_options_chooser(self, option_type: BidsOptions.Type):
        clear_layout(self.layout)
        # TODO add some factory to choose optionsFile and Folder class's base on data set folder
        self.bids_options_chooser = PretermOptionsFile() if option_type == BidsOptions.Type.FILE else PretermOptionsFolder()
        widget = OptionsChooser(self.bids_options_chooser,
                                subject_name=self.bids_subject.get_full_name(),
                                subject_key=self.get_current_subject_key())
        widget.path_modified.connect(self.bids_file.set_file_path)
        widget.bttn_finish.clicked.connect(self.finish)
        widget.bttn_back.clicked.connect(self.show_options_chooser_wrapper)
        self.layout.addWidget(widget)

    def finish(self):
        is_data_filled = self.bids_options_chooser.is_last_selected()
        if not is_data_filled:
            show_warn_message("Oops", "Please finish filling the form")
        print('data:')
        print(self.bids_options_chooser.get_data())
        print('data valid: ' + str(is_data_filled))
        print()
        print('file chosen is: ' + self.bids_file.get_file_path())
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
