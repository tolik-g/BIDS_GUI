from PyQt5.QtWidgets import *


class SubjectStatus(QWidget):
    """
    status line composed of QLabels
    to visually indicate current working subject
    """
    def __init__(self, *args, subject_name: str, subject_key: str,
                 resource=None, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # name
        name_str = 'name: {}'.format(subject_name)
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