class BidsOptions:
    # TODO rename to meaningful options, both keys and values
    OPTION_A = "OptionA"
    OPTION_B = "OptionB"

    def __init__(self):
        self.options = {BidsOptions.OPTION_A: ['A', 'B', 'C'], BidsOptions.OPTION_B: ['D', 'E', 'F']}
        self.selected = {BidsOptions.OPTION_A: 0, BidsOptions.OPTION_B: 0}

    def get_selected(self, key):
        try:
            return self.selected[key]
        except KeyError:
            return 0

    def set_selected(self, key, value):
        self.selected[key] = value
