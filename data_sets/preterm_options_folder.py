from data.bids_options import BidsOptions


class PretermOptionsFolder(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'type': ['fmri'],
                        'fmri': ['anatomy', 'functional', 'dwi'],
                        'functional': ['empathy', 'resting state', 'synchrony']
                        }
        self.option_type = BidsOptions.Type.FOLDER
        self.mode_type = BidsOptions.Mode.SINGLE
