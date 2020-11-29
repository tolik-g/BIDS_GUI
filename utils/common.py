from PyQt5.QtWidgets import (QMessageBox, QComboBox, QLabel, QFrame, QWidget,
                             QHBoxLayout, QSizePolicy)
from data.bids_options import BidsOptions


def show_warn_message(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


def create_drop_down_option(key: str, options: BidsOptions):
    label = QLabel(key)
    box = QComboBox()
    box.addItems(options.options[key])
    box.setCurrentIndex(options.get_selected(key))
    box.currentIndexChanged.connect(lambda index: options.set_selected(key, index))

    return label, box


class HLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)
