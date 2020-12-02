from data.bids_options import BidsOptions


class PretermOptionsFile(BidsOptions):
    def __init__(self):
        super().__init__()
        self.options = {'type': ['video']}

        self.mul_options_video = {'age': ['3 month', '6 month'],
                                  'interaction type': ['play', 'conflict', 'fun day'],
                                  'order': ['self-other', 'other-self']
                                  }

        self.mul_options = {'video': self.mul_options_video}
        self.option_type = BidsOptions.Type.FILE
        self.mode_type = BidsOptions.Mode.MUL
