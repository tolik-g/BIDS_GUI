from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from PyQt5.QtCore import pyqtSignal as Signal
from ui.separation_lines import HLine


class OptionWidget(QWidget):
    # signal should pass label, option
    option_selected = Signal(str, str)

    def __init__(self, *args, label, options, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = label
        self.selected_option = None
        self.label_widget = QLabel('Choose {}:'.format(label))
        self.options = []  # add radio buttons here?

        self.setup_ui(label, options)

    def setup_ui(self, label, options):
        self.layout.addWidget(self.label_widget)
        for option in options:
            radio_button = QRadioButton(option)
            radio_button.clicked.connect(self.emit_clicked)
            self.layout.addWidget(radio_button)
        self.layout.addWidget(HLine())

    def emit_clicked(self):
        radio_bttn = self.sender()
        self.selected_option = radio_bttn.text()
        self.option_selected.emit(self.label, self.selected_option)


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions):
        super().__init__()
        # layouts
        self.layout = QVBoxLayout()
        wrapper_layout = QVBoxLayout()
        wrapper_layout.addLayout(self.layout)
        wrapper_layout.addStretch()
        self.setLayout(wrapper_layout)

        # fields
        self.options = options
        self.selection_stack = []

        self.on_selection_clicked('', 'type')

    def on_selection_clicked(self, label, option):
        # check if selected option is a leaf
        if not self.options.get_options(option):
            return
        try:
            index = self.selection_stack.index(label)
        except ValueError:
            index = 0
        # remove widgets from layout and label from selection stack
        for i in range(self.layout.count()-1, index+1, -1):
            item = self.layout.takeAt(i)
            item.widget().deleteLater()
        self.selection_stack = self.selection_stack[:index+1]

        # add to the selection stack and create and add new OptionWidget
        self.selection_stack.append(option)
        option_widget = OptionWidget(label=option,
                                     options=self.options.get_options(option))
        option_widget.option_selected.connect(self.on_selection_clicked)
        self.layout.addWidget(option_widget)

    def get_data(self):
        data = {}
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            data[widget.label] = widget.selected_option
        return data






