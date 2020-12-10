from PyQt5.QtWidgets import *


def validate_structure_rec(structure, key, key_seen, val_seen):
    if not key in structure or type(structure[key]) is list:
        return True
    seen.append(key)
    for elem in structure[key]:
        if key_seen.count(elem) > 2:
            return False
        key_seen.append(key)
        if not validate_structure_rec(structure, elem, key_seen):
            return False
    return True


def validate_structure(structure):
    if 'root' not in structure:
        return False
    seen = []
    return validate_structure_rec(structure, 'root', seen)


class OptionSelector(QWidget):
    def __init__(self, label: str, options: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # setup label and option selection
        selector_label = QLabel(label)
        selector_options = QComboBox()
        selector_options.addItems(options)
        # complete widget setup (layout etc.)
        layout = QHBoxLayout()
        layout.addWidget(selector_label)
        layout.addWidget(selector_options)
        self.setLayout(layout)


class DestinationOptions(QWidget):
    """
    Structure is a dict defining the relationship between the
    different options, structure has the following constraints:
    - the root key is always named 'root'
    - (key: list) indicates that the value is a list of option
        selection labels.
    - (key: dict) indicates that the value is a list of options
        to chose from for a single option selector.
    - the dict is a tree, i.e. there is a unique route leading
        from the root to every leaf and every node has a unique value.
    """
    def __init__(self, structure, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.setLayout(layout)

    def populate_widget(self, structure):


