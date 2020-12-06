from data.bids_options import BidsOptions


class FulltermOptionsFolder(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'type': ['fmri'],
                        'fmri': ['anatomy', 'functional', 'DWI'],
                        'functional': ['Rest', 'Empathy', 'SO Interaction', 'Serial subtraction']
                        }
        self.option_type = BidsOptions.Type.FOLDER
        self.mode_type = BidsOptions.Mode.SINGLE