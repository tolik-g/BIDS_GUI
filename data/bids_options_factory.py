# TODO: complete rework :')
from data.bids_options import BidsOptions


class BidsOptionsFactory:

    def __init__(self):
        self.data_set = None

    def set_data_set(self, data_set: str):
        self.data_set = data_set

    def get_data_set(self):
        return self.data_set

    def get_bids_options(self, option_type: BidsOptions.Type):
        if self.data_set == 'preterm':
            return PretermOptionsFile() if option_type == BidsOptions.Type.FILE else PretermOptionsFolder()
        elif self.data_set == 'fullterm':
            return FulltermOptionsFile() if option_type == BidsOptions.Type.FILE else FulltermOptionsFolder()
        else:
            print('for debug purpose - falling back to Preterm')
            return PretermOptionsFile() if option_type == BidsOptions.Type.FILE else PretermOptionsFolder()