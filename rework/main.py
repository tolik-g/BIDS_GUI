from rework.utils_unsorted import *
from ui.drag_and_drop import DragDropArea
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup layouts
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
        self.layout_destination.addWidget(QPushButton('sample'))

        # layout origin
        # -this layout is responsible for subject picking,
        #  file picking, and dataset picking.
        project_subject_chooser = ProjectSubjectSelect()

        names_path = os.path.dirname(os.path.abspath(__file__))
        names_path = os.path.join(names_path, 'random_names.txt')
        with open(names_path, mode='r') as file:
            names = file.readlines()

        project_subject_chooser.update_subject_list(names)


        drag_n_drop = DragDropArea('file')
        save_bttn = SaveButton()
        self.layout_origin.addWidget(project_subject_chooser)
        self.layout_origin.addWidget(HLine())
        self.layout_origin.addWidget(drag_n_drop)
        self.layout_origin.addStretch()
        self.layout_origin.addWidget(save_bttn)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
