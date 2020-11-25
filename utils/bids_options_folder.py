from utils.bids_options import BidsOptions


class BidsOptionsFolder(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'folder1': ['A', 'B', 'C'], 'folder2': ['D', 'E', 'F']}
        self.init_selected()
