from PyQt5.QtWidgets import *


class OptionsChooserWrapper(QFrame):
    def __init__(self):
        super().__init__()
        # TODO enlarge file and folder buttons
        # layouts
        self.layout_main = QVBoxLayout()
        self.layout_navigation_bttns = QGridLayout()
        self.layout_center = QGridLayout()

        self.layout_main.addLayout(self.layout_center)
        self.layout_main.addLayout(self.layout_navigation_bttns)
        self.setLayout(self.layout_main)

        # center layout setup
        self.bttn_file = QPushButton('File')
        policy = QSizePolicy.Expanding
        self.bttn_file.setSizePolicy(policy, policy)
        self.bttn_folder = QPushButton('Folder')
        self.bttn_folder.setSizePolicy(policy, policy)
        self.layout_center.addWidget(self.bttn_file, 1, 1)
        self.layout_center.addWidget(self.bttn_folder, 1, 2)

        # navigation layout setup
        self.bttn_back = QPushButton('back')
        self.layout_navigation_bttns.setColumnStretch(1, 1)
        self.layout_navigation_bttns.addWidget(self.bttn_back, 0, 0)
