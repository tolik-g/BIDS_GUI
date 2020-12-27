from PyQt5.QtWidgets import *
from ui.options_chooser import OptionsChooser
from utils.config_loader import *
from ui.dataset_subject_chooser import DatasetSubjectChooser
from ui.drag_and_drop import DragDropArea
from ui.finish_button import FinishButton
from ui.separation_lines import HLine, VLine
from data.bids_key_file import BidsKeyFile
from data.bids_options import BidsOptions
import sys
import os

BIDS_KEY = 'BIDS_KEYS.csv'


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.key_file = BidsKeyFile()
        self.dataset_subject_chooser = DatasetSubjectChooser()
        self.finish_bttn = FinishButton()
        self.bids_options = None
        self.options_chooser = None
        self.drag_n_drop = DragDropArea()
        self.user_file_path = ''
        self.user_dataset = 'preterm'

        # setup connections
        self.setup_connections()

        # layouts
        self.layout_origin = QVBoxLayout()
        self.layout_destination = QVBoxLayout()
        self.layout_main = QHBoxLayout()
        self.populate_layouts()

        # setup central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)

        # more generic setup
        self.resize(800, 900)
        self.show()

    def populate_layouts(self):
        # layout main
        self.layout_main.addLayout(self.layout_origin)
        self.layout_main.addWidget(VLine())
        self.layout_main.addLayout(self.layout_destination)
        self.layout_main.setStretch(0, 1)
        self.layout_main.setStretch(2, 1)

        # layout destination
        # -this layout is responsible for determining where
        #  the file will be moved, it's name etc.
        self.options_chooser = OptionsChooser(self.bids_options)
        self.layout_destination.addWidget(self.options_chooser)

        # layout origin
        # -this layout is responsible for subject picking,
        #  file picking, and dataset picking.
        self.layout_origin.addWidget(self.dataset_subject_chooser)
        self.layout_origin.addWidget(HLine())
        self.layout_origin.addWidget(self.drag_n_drop)
        self.layout_origin.addStretch()
        self.layout_origin.addWidget(self.finish_bttn)

    def change_user_path(self, v):
        self.user_file_path = v
        self.display_options()

    def change_user_dataset(self, v):
        self.user_dataset = v
        self.display_options()

    def setup_connections(self):
        """
        connect signals and different components that require interaction
        :return:
        """
        self.dataset_subject_chooser.dataset_changed.connect(
            self.change_user_dataset)
        datasets_ls = get_dataset_list()
        self.dataset_subject_chooser.update_dataset_list(datasets_ls)
        self.finish_bttn.clicked.connect(self.execute)
        self.drag_n_drop.path_modified.connect(self.change_user_path)

    def display_options(self):
        """
        change form and data configuration to comply with the new dataset
        when changed
        :return:
        """
        # check folder of file
        if self.user_file_path != '':
            option_type = BidsOptions.Type.FOLDER if os.path.isdir(self.user_file_path) else BidsOptions.Type.FILE
        else:
            option_type = BidsOptions.Type.FOLDER
        # update options widget
        if self.options_chooser:
            index = self.layout_destination.indexOf(self.options_chooser)
            self.options_chooser.deleteLater()
            self.bids_options = get_bids_options(option_type,
                                                 self.user_dataset)
            self.options_chooser = OptionsChooser(self.bids_options)
            self.layout_destination.insertWidget(index, self.options_chooser)
        else:
            self.bids_options = get_bids_options(option_type,
                                                 self.user_dataset)
            self.options_chooser = OptionsChooser(self.bids_options)

        # check that the specified dataset path exists
        path = os.path.join(get_root_path(), self.user_dataset)
        assert os.path.isdir(path), 'dataset path does not exist'

        # check that dataset directory contains BIDS_KEY.csv file
        err_msg = "{} was not found in {}".format(BIDS_KEY, path)
        assert os.path.isfile(os.path.join(path, BIDS_KEY)), err_msg

        # set the bids key file to the dataset's key file
        self.key_file.set_file(os.path.abspath(os.path.join(path, BIDS_KEY)))

        # update subject chooser widget with updated subject names
        subj_names = self.key_file.get_subjects_names()
        self.dataset_subject_chooser.update_subject_list(subj_names)

    def execute(self):
        """
        take action based on the values submitted in the form.
        :return:
        """
        data = self.dataset_subject_chooser.get_data()
        data['subject key'] = self.key_file.subject_to_key(data['subject'])
        options_data = self.options_chooser.get_data()
        # TODO: change this into some actual action
        for key, val in data.items():
            print('{}: {},'.format(key, val))
        for key, val in options_data.items():
            print('{}: {},'.format(key, val))


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
