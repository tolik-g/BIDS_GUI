from enum import Enum


class BidsOptions:
    class Type(Enum):
        FILE = 1
        FOLDER = 2

    def __init__(self):
        self.options = {}
        self.selected = {}
        self.option_type = None

    def get_type(self):
        return self.option_type

    def init_selected(self):
        for key in self.options:
            self.selected[key] = 0

    def get_selected(self, key):
        try:
            return self.selected[key]
        except KeyError:
            return 0

    def set_selected(self, key, value):
        self.selected[key] = value

    def is_single_option_selected(self):
        selected_counter = 0
        for k in self.selected:
            if self.selected[k] > 0:
                selected_counter += 1
        return selected_counter == 1
