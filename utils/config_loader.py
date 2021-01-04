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


def get_dataset_list():
    with open('config.json') as json_file:
        data = json.load(json_file)
        dataset_ls = data['dataset']
        assert isinstance(dataset_ls, list), 'dataset keyword should correspond to a list'
        return dataset_ls


def get_root_path():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data['root path']
