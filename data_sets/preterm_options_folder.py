from data.bids_options import BidsOptions


class PretermOptionsFolder(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'type': ['fmri', 'other1'],
                        'fmri': ['anatomy', 'functional', 'dwi'],
                        'other1': ['other2'],
                        'other2': ['other3'],
                        }
        self.option_type = BidsOptions.Type.FOLDER
        self.mode_type = BidsOptions.Mode.SINGLE
