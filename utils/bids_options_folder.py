from utils.bids_options import BidsOptions


class BidsOptionsFolder(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'video': ['none', 'todo'],
                        'fmri': ['none', 'anatomy', 'functional', 'dti']}
        self.init_selected()
        self.option_type = BidsOptions.Type.FOLDER
