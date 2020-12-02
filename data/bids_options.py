from enum import Enum


class BidsOptions:
    class Type(Enum):
        FILE = 1
        FOLDER = 2

    class Mode(Enum):
        SINGLE = 1
        MUL = 2

    def __init__(self):
        self.options = {}
        self.mul_options = {}
        self.selected_mul_options = {}
        self.selected_single_option = ''
        self.selected_main_key = ''
        self.option_type = None
        self.mode_type = None

    def get_type(self):
        return self.option_type

    def get_mode(self):
        return self.mode_type

    def set_main_key(self, key: str):
        self.selected_main_key = key

    def init_mul_selected(self, first_key: str):
        for key in self.mul_options[first_key]:
            self.selected_mul_options[key] = 0

    def set_mul_selected(self, key, value):
        self.selected_mul_options[key] = value

    def get_options(self, key: str):
        try:
            return self.options[key]
        except KeyError:
            return None

    def set_single_selected(self, value: str):
        self.selected_main_key = self.selected_single_option
        self.selected_single_option = value

    def is_last_selected(self):
        return self.get_options(self.selected_single_option) is None

    def get_data(self):
        options = self.selected_single_option if self.mode_type == BidsOptions.Mode.SINGLE else self.selected_mul_options
        return self.selected_main_key, options
