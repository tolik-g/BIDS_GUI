from utils.bids_options import BidsOptions


class BidsOptionsFile(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'demographic': ['none', 'csv', 'spss', 'excel'],
                        'fmri': ['none', 'anatomy', 'functional', 'dti']}
        self.init_selected()
        self.option_type = BidsOptions.Type.FILE
