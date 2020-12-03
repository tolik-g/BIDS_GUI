from PyQt5.QtWidgets import QMessageBox, QFrame, QLabel, QComboBox
from data.bids_options import BidsOptions
import dicom2nifti
import os


def show_warn_message(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


def create_drop_down_option(first_key: str, second_key: str, options: BidsOptions):
    label = QLabel(second_key)
    box = QComboBox()
    box.addItems(options.mul_options[first_key][second_key])
    box.currentIndexChanged.connect(lambda index: options.set_mul_selected(second_key, index))

    return label, box


def clear_layout(layout):
    for i in range(layout.count())[::-1]:
        item = layout.takeAt(i)
        item.widget().deleteLater()


class HLine(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)


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
