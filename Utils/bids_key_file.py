import pandas as pd


class BidsKeyFile:
    def __init__(self):
        self.key_path = ''

    def get_file(self):
        return self.key_path

    def set_file(self, file):
        self.key_path = file
