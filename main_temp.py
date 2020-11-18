from PyQt5.QtWidgets import *
import sys
from directory_decider.directory_decider import DirectoryDecider
from PyQt5 import QtGui


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # generic layout/widget setup for QMainWindow
        self.layout = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.setWindowTitle('BIDS GUI')
        self.setWindowIcon(QtGui.QIcon('Icons/title.png'))
        self.setMinimumSize(600, 600)
        self.layout.addWidget(DirectoryDecider(), 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
