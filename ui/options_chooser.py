from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from PyQt5.QtCore import pyqtSignal as Signal
from ui.separation_lines import HLine
from utils.common import create_drop_down_option


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

        self.setup_ui(first_key, pairs)

    def setup_ui(self, first_key, pairs):
        row = 0
        self.layout.addWidget(QLabel(first_key))
        row += 1
        for pair in pairs:
            self.layout.addWidget(pair[0], row, 0)
            self.layout.addWidget(pair[1], row, 1)
            row += 1


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
        try:
            index = self.selection_stack.index(label)
            _, _ = self.options.set_single_selected(option)
        except ValueError:
            index = 0
        # remove widgets from layout and label from selection stack
        for i in range(self.layout.count()-1, index, -1):
            item = self.layout.takeAt(i)
            item.widget().deleteLater()
        self.selection_stack = self.selection_stack[:index+1]

        # check if selected option is a leaf
        if not self.options.get_options(option):
        # if self.options.is_last(option):
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
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            data[widget.label] = widget.selected_option
        return data


# from PyQt5.QtWidgets import *
# from data.bids_options import BidsOptions
# from utils.common import create_drop_down_option
#
#
# class OptionsChooser(QFrame):
#     def __init__(self, options: BidsOptions):
#         super().__init__()
#         # layouts
#         self.layout_selection = QGridLayout()
#         self.selection_label = None
#         self.options = options
#         self.setLayout(self.layout_selection)
#         self.widgets = []
#
#         # selection layout setup
#         self.set_new_selection_list('type', options.get_options('type'))
#
#     def remove_widgets(self, index_: int):
#         remove_list = self.widgets[index_:]
#         for inter_list in remove_list:
#             for widget_ in inter_list:
#                 widget_.setParent(None)
#
#         self.widgets = self.widgets[:index_]
#
#     def on_selection_clicked(self):
#         radioBtn = self.sender()
#         if radioBtn.isChecked():
#             selected = radioBtn.text()
#             is_delete, delete_index = self.options.set_single_selected(selected)
#             is_delete and self.remove_widgets(delete_index)
#             is_last = self.options.is_last(selected)
#             if not is_last:
#                 next_list = self.options.get_options(selected)
#                 self.set_new_selection_list(selected, next_list)
#             elif self.options.get_mode() == BidsOptions.Mode.MUL:
#                 self.options.init_mul_selected(selected)
#                 self.set_new_dropdown(selected)
#
#     def set_new_selection_list(self, key, button_list):
#         if button_list is None:
#             return
#         widget_list = []
#         label = QLabel('Choose ' + key + ':')
#         widget_list.append(label)
#         self.layout_selection.addWidget(label)
#         for button_label in button_list:
#             button = QRadioButton(button_label)
#             button.toggled.connect(self.on_selection_clicked)
#             self.layout_selection.addWidget(button)
#             widget_list.append(button)
#         self.widgets.append(widget_list)
#
#     def set_new_dropdown(self, first_key):
#         widget_list = []
#         label = QLabel('Fill ' + first_key + ':')
#         widget_list.append(label)
#         self.layout_selection.addWidget(label, 0, 0)
#         for index, key in enumerate(self.options.mul_options[first_key]):
#             label, dropdown = create_drop_down_option(first_key, key, self.options)
#             self.layout_selection.addWidget(label, index + 1, 0)
#             self.layout_selection.addWidget(dropdown, index + 1, 1)
#             widget_list.append(label)
#             widget_list.append(dropdown)
#         self.widgets.append(widget_list)