from PyQt5.QtWidgets import QMessageBox, QFrame, QLabel, QComboBox

from data.bids_options import BidsOptions


def show_warn_message(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


def create_drop_down_option(first_key: str, second_key: str, options: BidsOptions):
    label = QLabel(second_key)
    box = QComboBox()
    box.addItems(options.mul_options[first_key][second_key])
    box.currentIndexChanged.connect(lambda index: options.set_mul_selected(second_key, index))

    return label, box


def clear_layout(layout):
    for i in range(layout.count())[::-1]:
        item = layout.takeAt(i)
        item.widget().deleteLater()


class HLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)


