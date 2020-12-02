from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from utils.common import clear_layout, create_drop_down_option
from utils.subject_status import SubjectStatus
from utils.drag_and_drop import DragDropArea


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions, subject_name: str,
                 subject_key: str):
        super().__init__()
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()
        self.layout_browse = QGridLayout()
        self.layout_selection = QGridLayout()
        self.selection_label = None
        self.options = options

        # populate layout_main
        subject_status = SubjectStatus(subject_name=subject_name,
                                       subject_key=subject_key)
        self.layout_main.addWidget(subject_status)
        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # drag and drop/ browse layout setup
        text_title = 'file' if options.get_type() == BidsOptions.Type.FILE else 'folder'
        self.drag_area = DragDropArea(text_title=text_title)
        self.drag_area.path_modified.connect(subject_status.mod_resource)
        self.path_modified = self.drag_area.path_modified
        self.layout_browse.addWidget(self.drag_area, 0, 1)
        self.layout_browse.setColumnStretch(0, 1)
        self.layout_browse.setColumnStretch(2, 1)

        # selection layout setup
        self.set_new_selection_list('type', options.get_options('type'), 0)

        # center layout setup
        self.layout_center.setRowStretch(0, 1)
        self.layout_center.setRowStretch(4, 1)
        self.layout_center.setColumnStretch(0, 1)
        self.layout_center.setColumnStretch(1, 1)
        self.layout_center.setColumnStretch(4, 1)
        self.layout_center.setColumnStretch(5, 1)
        self.layout_center.addLayout(self.layout_browse, 1, 1, 1, 4)
        self.layout_center.setRowMinimumHeight(2, 50)
        self.layout_center.addLayout(self.layout_selection, 3, 2, 1, 2)

        # navigation layout setup
        self.bttn_finish = QPushButton('finish')
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
        self.layout_navigation_bttns.addWidget(self.bttn_finish, 0, 2)

    def on_selection_clicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            selected = radioBtn.text()
            self.options.set_single_selected(selected)
            is_last = self.options.is_last_selected()
            if not is_last:
                next_list = self.options.get_options(selected)
                self.set_new_selection_list(selected, next_list, 300)
            elif self.options.get_mode() == BidsOptions.Mode.MUL:
                self.options.init_mul_selected(selected)
                QTimer.singleShot(300, lambda: self.set_new_dropdown(selected))

    def set_new_selection_list(self, key, button_list, delay: int):
        if button_list is None:
            return
        QTimer.singleShot(delay, lambda: self.set_new_selection_list_job(key, button_list))

    def set_new_selection_list_job(self, key, button_list):
        clear_layout(self.layout_selection)
        self.selection_label = QLabel('Choose ' + key + ':')
        self.layout_selection.addWidget(self.selection_label)
        for button_label in button_list:
            button = QRadioButton(button_label)
            button.toggled.connect(self.on_selection_clicked)
            self.layout_selection.addWidget(button)

    def set_new_dropdown(self, first_key):
        clear_layout(self.layout_selection)
        self.selection_label = QLabel('Fill ' + first_key + ':')
        self.layout_selection.addWidget(self.selection_label, 0, 0)
        self.options.set_main_key(first_key)
        for index, key in enumerate(self.options.mul_options[first_key]):
            label, dropdown = create_drop_down_option(first_key, key, self.options)
            self.layout_selection.addWidget(label, index + 1, 0)
            self.layout_selection.addWidget(dropdown, index + 1, 1)
