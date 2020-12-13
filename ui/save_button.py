from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class SaveButton(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.save_bttn = QPushButton('save')

        # signals
        # emits signal when the save button is clicked
        self.clicked = self.save_bttn.clicked

        # generic widget setup
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.save_bttn)
        self.layout.addStretch()

    def toggle(self, toggle: bool):
        """
        toggle if the save button can be pressed
        :param toggle: True = enabled, False = Disabled
        :return:
        """
        self.save_bttn.setEnabled(toggle)
