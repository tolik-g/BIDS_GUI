from utils.bids_options import BidsOptions


class BidsOptionsFile(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'file1': ['A', 'B', 'C'], 'file2': ['D', 'E', 'F']}
        self.init_selected()
