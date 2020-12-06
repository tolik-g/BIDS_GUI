from PyQt5.QtWidgets import *


class OptionsStatus(QWidget):
    """
    status line composed of QLabels
    to visually indicate current working subject
    """
    def __init__(self, *args, subject_name: str, subject_key: str,
                 data_set: str, resource=None, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # data set
        data_set_str = 'Dataset: {}'.format(data_set)
        layout.addWidget(QLabel(data_set_str))

        # name
        name_str = '| Subject: {}'.format(subject_name)
        layout.addWidget(QLabel(name_str))

        # code_id
        code_str = '| Key: {}'.format(subject_key)
        layout.addWidget(QLabel(code_str))

        # resource
        if resource is None:
            resource_str = ''
        else:
            resource_str = '| Resource: {}'.format(resource)
        self.resource = QLabel(resource_str)
        layout.addWidget(self.resource)

        layout.addStretch()

    def mod_resource(self, text: str):
        text_ls = text.split('/')
        # in case directory path ends with /
        if text_ls[-1]:
            resource = '| Resource: {}'.format(text_ls[-1])
        else:
            resource = '| Resource: {}'.format(text_ls[-2])
        self.resource.setText(resource)