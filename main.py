from PyQt5.QtWidgets import *
import json
from data.bids_options import BidsOptions
from utils.config_loader import get_bids_options, get_dataset_list, get_root_path
from ui.dataset_subject_chooser import DatasetSubjectChooser
from ui.drag_and_drop import DragDropArea
import sys
from ui.finish_button import FinishButton
from ui.separation_lines import HLine, VLine
from data.bids_key_file import BidsKeyFile
import os

BIDS_KEY = 'BIDS_KEYS.csv'


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.key_file = BidsKeyFile()
        self.dataset_subject_chooser = DatasetSubjectChooser()
        self.finish_bttn = FinishButton()

        # setup layouts
        self.layout_origin = QVBoxLayout()
        self.layout_destination = QVBoxLayout()
        self.layout_main = QHBoxLayout()
        self.populate_layouts()

        # setup connections
        self.setup_connections()

        # setup central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)

        # more generic setup
        self.resize(800, 900)
        self.show()
        # TODO connect others to this -> after Drag & Drop we can know if its a file or a folder
        get_bids_options(BidsOptions.Type.FOLDER, "preterm")

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
        self.layout_destination.addWidget(QPushButton('sample'))

        # layout origin
        # -this layout is responsible for subject picking,
        #  file picking, and dataset picking.
        drag_n_drop = DragDropArea()

        self.layout_origin.addWidget(self.dataset_subject_chooser)
        self.layout_origin.addWidget(HLine())
        self.layout_origin.addWidget(drag_n_drop)
        self.layout_origin.addStretch()
        self.layout_origin.addWidget(self.finish_bttn)

    def setup_connections(self):
        self.dataset_subject_chooser.dataset_changed.connect(
            self.select_dataset)
        datasets_ls = get_dataset_list()
        self.dataset_subject_chooser.update_dataset_list(datasets_ls)
        self.finish_bttn.clicked.connect(self.execute)

    def select_dataset(self, dataset):
        path = os.path.join(get_root_path(), dataset)
        assert os.path.isdir(path), 'dataset path does not exist'
        err_msg = "{} was not found in {}".format(BIDS_KEY, path)
        assert os.path.isfile(os.path.join(path, BIDS_KEY)), err_msg
        abs_path_csv = os.path.abspath(os.path.join(path, BIDS_KEY))
        self.key_file.set_file(abs_path_csv)
        subj_names = self.key_file.get_subjects_names()
        self.dataset_subject_chooser.update_subject_list(subj_names)

    def execute(self):
        data = self.dataset_subject_chooser.get_data()
        data['subject key'] = self.key_file.subject_to_key(data['subject'])
        # temp print out form values
        for key, val in data.items():
            print('{}: {},'.format(key, val))


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
