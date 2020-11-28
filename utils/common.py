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


class SubjectStatus(QWidget):
    """
    status line composed of QLabels
    to visually indicate current working subject
    """
    def __init__(self, *args, first_name: str, last_name: str, subject_key: str,
                 resource=None, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # name
        name_str = 'name: {} {}'.format(first_name, last_name)
        layout.addWidget(QLabel(name_str))

        # code_id
        code_str = '| key: {}'.format(subject_key)
        layout.addWidget(QLabel(code_str))

        # resource
        if resource is None:
            resource_str = ''
        else:
            resource_str = '| resource: {}'.format(resource)
        self.resource = QLabel(resource_str)
        layout.addWidget(self.resource)

        layout.addStretch()

    def mod_resource(self, text: str):
        text_ls = text.split('/')
        'in case directory path ends with /'
        if text_ls[-1]:
            resource = '| resource: {}'.format(text_ls[-1])
        else:
            resource = '| resource: {}'.format(text_ls[-2])
        self.resource.setText(resource)
