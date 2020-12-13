import json

from data.bids_options import BidsOptions


def get_bids_options(option_type: BidsOptions.Type, dataset: str):
    with open('config.json') as json_file:
        data = json.load(json_file)
        if dataset not in data['dataset']:
            return
        type_ = 'folder' if option_type == BidsOptions.Type.FOLDER else 'file'
        options_ = data[dataset][type_]['options']
        mode_ = data[dataset][type_]['mode']
        try:
            mul_options_ = data[dataset][type_]['mul_options']
        except KeyError:
            mul_options_ = {}

        return BidsOptions(type_, mode_, options_, mul_options_)


class BidsOptionsLoader:
    def __init__(self):
        pass
