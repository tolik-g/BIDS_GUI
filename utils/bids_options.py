from enum import Enum


class BidsOptions:
    class Type(Enum):
        FILE = 1
        FOLDER = 2

    def __init__(self):
        self.options = {}
        self.selected = {}

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
