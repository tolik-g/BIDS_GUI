from data.bids_options import BidsOptions


class FulltermOptionsFile(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'type': ['TODO']}

        self.mul_options = {'TODO': {'A': ['a', 'b']}}
        self.option_type = BidsOptions.Type.FILE
        self.mode_type = BidsOptions.Mode.MUL
