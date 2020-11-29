from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from utils.common import create_drop_down_option
from utils.drag_and_drop import DragDropArea
from utils.subject_status import SubjectStatus


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions,
                 subject_status: SubjectStatus):
        super().__init__()

        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()
        self.layout_title = QGridLayout()
        self.layout_browse = QGridLayout()
        self.layout_dropdown = QGridLayout()

        self.layout_main.addWidget(subject_status)
        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # browse layout setup
        text_title = 'file' if options.get_type() == BidsOptions.Type.FILE else 'folder'
        self.drag_area = DragDropArea(text_title=text_title)
        self.drag_area.path_modified.connect(subject_status.mod_resource)
        self.layout_browse.addWidget(self.drag_area, 0, 1)
        self.layout_browse.setColumnStretch(0, 1)
        self.layout_browse.setColumnStretch(2, 1)

        # dropdown layout setup
        for index, key in enumerate(options.options):
            label, dropdown = create_drop_down_option(key, options)
            self.layout_dropdown.addWidget(label, index, 0)
            self.layout_dropdown.addWidget(dropdown, index, 1)

        # center layout setup
        self.layout_center.setRowStretch(0, 1)
        self.layout_center.setRowStretch(4, 1)
        self.layout_center.setColumnStretch(0, 1)
        self.layout_center.setColumnStretch(1, 1)
        self.layout_center.setColumnStretch(4, 1)
        self.layout_center.setColumnStretch(5, 1)
        self.layout_center.addLayout(self.layout_browse, 1, 1, 1, 4)
        self.layout_center.setRowMinimumHeight(2, 50)
        self.layout_center.addLayout(self.layout_dropdown, 3, 2, 1, 2)

        # navigation layout setup
        self.bttn_finish = QPushButton('finish')
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
        self.layout_navigation_bttns.addWidget(self.bttn_finish, 0, 2)
