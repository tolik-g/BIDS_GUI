from data.bids_options import BidsOptions
from data_sets.fullterm_options_file import FulltermOptionsFile
from data_sets.fullterm_options_folder import FulltermOptionsFolder
from data_sets.preterm_options_file import PretermOptionsFile
from data_sets.preterm_options_folder import PretermOptionsFolder


class BidsOptionsFactory:
    DATASETS = ['preterm', 'fullterm', 'Downloads', 'EEG_MOM_CHLD_IV4615_053_170320 (2)']

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

