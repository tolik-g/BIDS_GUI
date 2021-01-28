from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QLabel, QComboBox
from data.bids_options import BidsOptions
from PyQt5 import QtGui


def msg_box_icon(msg, success: bool):
    if success:
        msg.setIconPixmap(QPixmap('assets/valid_big.png'))
    else:
        msg.setIconPixmap(QPixmap('assets/invalid_big.png'))


def show_message(title, text, success=False):
    msg = QMessageBox()
    msg.setWindowIcon(QtGui.QIcon('assets/title.png'))
    msg_box_icon(msg, success)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


def create_drop_down_option(first_key: str, second_key: str, options: BidsOptions):
    label = QLabel(second_key)
    box = QComboBox()
    box.addItems(options.mul_options[first_key][second_key])
    box.currentIndexChanged.connect(lambda index: options.set_mul_selected(second_key, index))

    return label, box
