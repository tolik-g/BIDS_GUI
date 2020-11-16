from PyQt5.QtWidgets import *
import sys
from directory_decider.directory_decider import DirectoryDecider
from directory_decider.subj_mapping import SubjMapping


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
        self.setWindowTitle('Temp Generic Main')
        dd = DirectoryDecider()
        self.layout.addWidget(dd, 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
