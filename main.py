from PyQt5.QtWidgets import *
import sys
from ui.manager import Manager
from PyQt5 import QtGui
from utils.styles import STYLE


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
        self.setStyleSheet(STYLE)
        self.setWindowTitle('BIDS GUI')
        self.setWindowIcon(QtGui.QIcon('icons/title.png'))
        self.setMinimumSize(600, 600)
        self.layout.addWidget(Manager(), 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
