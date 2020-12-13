from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class FinishButton(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # fields
        self.finish_bttn = QPushButton('finish')

        # signals
        # emits signal when the save button is clicked
        self.clicked = self.finish_bttn.clicked

        # generic widget setup
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.finish_bttn)
        self.layout.addStretch()

    def toggle(self, toggle: bool):
        """
        toggle if the finish button can be pressed
        :param toggle: True = enabled, False = Disabled
        :return:
        """
        self.finish_bttn.setEnabled(toggle)
