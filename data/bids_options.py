from enum import Enum


class BidsOptions:
    class Type(Enum):
        FILE = 1
        FOLDER = 2

    class Mode(Enum):
        SINGLE = 1
        MUL = 2

    def __init__(self, type_: Type, mode_, options_, mul_options_):
        self.options = options_
        self.mul_options = mul_options_
        self.selected_mul_options = {}
        self.selected_singles = []
        self.last_key = ''
        self.type = type_
        self.mode = mode_

    def get_type(self):
        return self.type

    def get_mode(self):
        return self.mode

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
        if len(self.selected_singles) > 0:
            is_same_key = False
            for key, values in self.options.items():
                if value in values and self.selected_singles[-1] in values:
                    is_same_key = True
                    break
            is_same_key and self.selected_singles.pop()

        self.selected_singles.append(value)

    def is_last_selected(self):
        return len(self.selected_singles) > 0 and self.get_options(self.selected_singles[-1]) is None

    def get_data(self):
        copy_list = self.selected_singles.copy()
        if self.mode == BidsOptions.Mode.MUL:
            copy_list.append(self.selected_mul_options)
        return copy_list
