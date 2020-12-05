from PyQt5.QtWidgets import *


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
        self.show()

    def populate_layouts(self):
        # layout main
        self.layout_main.addLayout(self.layout_origin)
        self.layout_main.addLayout(self.layout_destination)

        # layout destination
        ## this layout is responsible for determining where
        ## the file will be moved, it's name etc.
        # TODO: add relevant widgets/layouts

        # layout origin
        ## this layout is responsible for subject picking,
        ## file picking, and dataset picking.
        # TODO: add relevant widgets/layouts



