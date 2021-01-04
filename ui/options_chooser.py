from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from PyQt5.QtCore import pyqtSignal as Signal
from ui.separation_lines import HLine
from utils.common import create_drop_down_option
from ui.session_chooser import SessionChooser


class OptionWidget(QWidget):
    # signal should pass label, option
    option_selected = Signal(str, str)

    def __init__(self, *args, label, options, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # fields
        self.label = label
        self.selected_option = None
        self.label_widget = QLabel('Choose {}:'.format(label))
        self.options = []  # add radio buttons here?

        self.setup_ui(options)

    def setup_ui(self, options):
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


class DropdownWidget(QWidget):
    def __init__(self, *args, first_key, pairs, **kwargs):
        super().__init__(*args, **kwargs)
        # layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # fields
        self.label = first_key
        self.pairs = pairs

        self.setup_ui(first_key)

    def setup_ui(self, first_key):
        row = 0
        self.layout.addWidget(QLabel(first_key))
        row += 1
        for pair in self.pairs:
            self.layout.addWidget(pair[0], row, 0)
            self.layout.addWidget(pair[1], row, 1)
            row += 1


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions, sessions=None):
        super().__init__()
        # fields
        if sessions is None:
            sessions = ['nicu', '3m', '6m', '12m', '24m', '5y', '10y', '18yHV', '18yScan']
        self.session_chooser = SessionChooser(session_ls=sessions)
        self.options = options
        self.selection_stack = []

        # layouts
        self.layout = QVBoxLayout()
        wrapper_layout = QVBoxLayout()
        wrapper_layout.addWidget(self.session_chooser)
        wrapper_layout.addWidget(HLine())

        wrapper_layout.addLayout(self.layout)
        wrapper_layout.addStretch()
        self.setLayout(wrapper_layout)

        self.on_selection_clicked('', 'type')

    def on_selection_clicked(self, label, option):
        try:
            index = self.selection_stack.index(label)
            self.options.set_single_selected(option)
        except ValueError:
            index = 0
        # remove widgets from layout and label from selection stack
        for i in range(self.layout.count()-1, index, -1):
            item = self.layout.takeAt(i)
            item.widget().deleteLater()
        self.selection_stack = self.selection_stack[:index+1]

        # check if selected option is a leaf
        if self.options.is_last(option):
            # handle MUL case
            if self.options.get_mode() == BidsOptions.Mode.MUL:
                self.options.init_mul_selected(option)
                dropdown_widget = self.generate_dropdown_widget(option)
                self.selection_stack.append(option)
                self.layout.addWidget(dropdown_widget)
            return

        # add to the selection stack and create and add new OptionWidget
        self.selection_stack.append(option)
        option_widget = OptionWidget(label=option,
                                     options=self.options.get_options(option))
        option_widget.option_selected.connect(self.on_selection_clicked)
        self.layout.addWidget(option_widget)

    def generate_dropdown_widget(self, first_key):
        pairs = []
        for second_key in self.options.mul_options[first_key]:
            label, dropdown = create_drop_down_option(first_key, second_key,
                                                      self.options)
            pairs.append((label, dropdown))
        return DropdownWidget(first_key=first_key, pairs=pairs)

    def get_data(self):
        data = {}
        data['session'] = self.session_chooser.get_session()
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, OptionWidget):
                data[widget.label] = widget.selected_option
            else:
                data_mult = {}
                for pair in widget.pairs:
                    data_mult[pair[0].text()] = pair[1].currentText()
                data[widget.label] = data_mult
        return data
