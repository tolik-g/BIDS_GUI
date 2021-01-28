import os

from data.bids_options import BidsOptions
from utils.common import show_message
from utils.files_manipulation import dcm_to_nifti

ROOT_PATH = 'sample_root'


def create_dir_if_not_exist(path_):
    if not os.path.isdir(path_):
        os.mkdir(path_)


def get_subject_path(data: dict):
    # TODO take session into account
    sub_path = os.path.join(ROOT_PATH, data['dataset'], data['subject_key'])
    create_dir_if_not_exist(sub_path)
    return sub_path


def execute_fmri(data: dict, sub_path: str):
    target_dir = ''
    output_filename = ''
    if data['fmri'] == 'anatomy':
        target_dir = os.path.join(sub_path, 'anat')
        output_filename = data['subject_key'] + '_T1w'
    elif data['fmri'] == 'functional':
        target_dir = os.path.join(sub_path, 'func')
        func_val = data['functional'].replace(' ', '_')
        output_filename = '{}_{}'.format(data['subject_key'], func_val)
    elif data['fmri'] == 'DWI':
        target_dir = os.path.join(sub_path, 'dwi')
        output_filename = data['subject_key'] + '_dwi'

    create_dir_if_not_exist(target_dir)
    return dcm_to_nifti(path_in=data['path'], path_out=target_dir, f_name=output_filename)


def execute_video(data: dict, sub_path: str):
    # TODO ask ruth about all video params + naming convention + dir path
    print(os.path.join(sub_path, 'video'))
    return True


def validate_edge_cases(data: dict):
    if data['dataset'] == 'preterm' and data['type'] == 'fmri' and data['session'] not in ['18yHV', '18yScan']:
        show_message('preterm error', 'session 18y is the only one possible on fmri data')
        return False
    return True


def execute(data: dict):
    for key, val in data.items():
        print('{}: {},'.format(key, val))

    if not validate_edge_cases(data):
        return False, ''

    subject_path = get_subject_path(data)
    if data['type'] == 'fmri':
        return execute_fmri(data, subject_path), subject_path
    elif data['type'] == 'video':
        return execute_video(data, subject_path), subject_path
