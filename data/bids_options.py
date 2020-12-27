from enum import Enum
from anytree import Node
from anytree.search import find


class BidsOptions:
    class Type(Enum):
        FILE = 1
        FOLDER = 2

    class Mode(Enum):
        SINGLE = 1
        MUL = 2

    def __init__(self, type_: Type, mode_, options_, mul_options_):
        self.options = {}
        self.mul_options = mul_options_
        self.selected_mul_options = {}
        self.selected_singles = []
        self.last_key = ''
        self.type = type_
        self.mode = BidsOptions.Mode.MUL if mode_ == 'MUL' else BidsOptions.Mode.SINGLE
        self.init_tree_options(options_)

    def recur_tree_init(self, options_, parent_str: str, parent):
        for key in options_[parent_str]:
            new_parent = Node(key, parent=parent)
            if key in options_:
                self.recur_tree_init(options_, key, new_parent)

    def init_tree_options(self, options_):
        self.options = Node("type")
        self.recur_tree_init(options_, "type", self.options)
        self.selected_singles.append("type")

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
        node_ = find(self.options, lambda node: node.name == key)
        child_list = []
        for child in node_.children:
            child_list.append(child.name)
        return child_list

    def is_parent(self, son: str, parent: str):
        son_ = find(self.options, lambda node: node.name == son)
        return parent == son_.parent.name

    def set_single_selected(self, value: str):
        index_ = 0
        if len(self.selected_singles) > 0:
            if not self.is_parent(value, self.selected_singles[-1]):
                for index, key in enumerate(self.selected_singles):
                    if self.is_parent(value, key):
                        index_ = index
                        break
                self.selected_singles = self.selected_singles[:index_ + 1]

        self.selected_singles.append(value)

    def is_last(self, key: str):
        node_ = find(self.options, lambda node: node.name == key)
        return node_.is_leaf

    def get_data(self):
        copy_list = self.selected_singles.copy()
        if self.mode == BidsOptions.Mode.MUL:
            copy_list.append(self.selected_mul_options)
        return copy_list
