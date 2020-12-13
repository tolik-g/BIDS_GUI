from utils.files_manipulation import dcm_to_nifti


class BidsFile:
    def __init__(self):
        self.file_path = ''

    def set_file_path(self, file_path):
        self.file_path = file_path

    def get_file_path(self):
        return self.file_path

    def move_dcm_folder(self, path_out, f_name, compression=True):
        dcm_to_nifti(self.file_path, path_out, f_name, compression)
