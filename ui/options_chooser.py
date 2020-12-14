from PyQt5.QtWidgets import *
from data.bids_options import BidsOptions
from utils.common import create_drop_down_option


class OptionsChooser(QFrame):
    def __init__(self, options: BidsOptions):
        super().__init__()
        # layouts
        self.layout_selection = QGridLayout()
        self.selection_label = None
        self.options = options
        self.setLayout(self.layout_selection)
        self.widgets = []

        # selection layout setup
        self.set_new_selection_list('type', options.get_options('type'))

    def remove_widgets(self, index_: int):
        remove_list = self.widgets[index_:]
        for inter_list in remove_list:
            for widget_ in inter_list:
                widget_.setParent(None)

        self.widgets = self.widgets[:index_]

    def on_selection_clicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            selected = radioBtn.text()
            is_delete, delete_index = self.options.set_single_selected(selected)
            is_delete and self.remove_widgets(delete_index)
            is_last = self.options.is_last(selected)
            if not is_last:
                next_list = self.options.get_options(selected)
                self.set_new_selection_list(selected, next_list)
            elif self.options.get_mode() == BidsOptions.Mode.MUL:
                self.options.init_mul_selected(selected)
                self.set_new_dropdown(selected)

    def set_new_selection_list(self, key, button_list):
        if button_list is None:
            return
        widget_list = []
        label = QLabel('Choose ' + key + ':')
        widget_list.append(label)
        self.layout_selection.addWidget(label)
        for button_label in button_list:
            button = QRadioButton(button_label)
            button.toggled.connect(self.on_selection_clicked)
            self.layout_selection.addWidget(button)
            widget_list.append(button)
        self.widgets.append(widget_list)

    def set_new_dropdown(self, first_key):
        widget_list = []
        label = QLabel('Fill ' + first_key + ':')
        widget_list.append(label)
        self.layout_selection.addWidget(label, 0, 0)
        for index, key in enumerate(self.options.mul_options[first_key]):
            label, dropdown = create_drop_down_option(first_key, key, self.options)
            self.layout_selection.addWidget(label, index + 1, 0)
            self.layout_selection.addWidget(dropdown, index + 1, 1)
            widget_list.append(label)
            widget_list.append(dropdown)
        self.widgets.append(widget_list)

