from PyQt5.QtWidgets import (QMessageBox, QComboBox, QLabel, QFrame, QWidget,
                             QHBoxLayout)
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


class SubjectStatus(QWidget):
    """
    status line composed of QLabels
    to visually indicate current working subject
    """
    def __init__(self, *args, name: str, last_name: str, code_id,
                 resource=None, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # name
        name_str = 'name: {} {}'.format(name, last_name)
        layout.addWidget(QLabel(name_str))

        # code_id
        code_str = '| code: {}'.format(code_id)
        layout.addWidget(QLabel(code_str))

        # resource
        if resource is None:
            self.resource_str = ''
        else:
            self.resource_str = '| resource: {}'.format(resource)
        layout.addWidget(QLabel(self.resource_str))

    def mod_resource(self, text: str):
        text = '| resource: {}'.format(text)
        self.resource_str.setText(text)
