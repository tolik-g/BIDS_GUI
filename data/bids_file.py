from utils.common import dcm_to_nifti


# TODO start add rules, 1. fmri folders 2. video files
class BidsFile:
    def __init__(self):
        self.file_path = ''

    def set_file_path(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path

    def move_dcm(self, path_out, f_name, compression=True):
        dcm_to_nifti(self.file_path, path_out, f_name, compression)
