import dicom2nifti
import os


def dcm_to_nifti(path_in, path_out, f_name, compression=True):
    """
    convert folder containing single dcm series to nifti file
    :param path_in: path to folder containing single dcm series
    :param path_out: output directory path
    :param f_name: file name without extension
    :param compression: boolean condition
    :return:
    """
    extension = '.nii.gz' if compression else '.nii'
    path_out_f = os.path.join(path_out, f_name + extension)
    try:
        dicom2nifti.dicom_series_to_nifti(path_in, path_out_f)
        return True
    except Exception as e:
        return False
