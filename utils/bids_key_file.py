import pandas as pd

from utils.bids_subject import BidsSubject


class BidsKeyFile:
    def __init__(self):
        self.key_path = ''
        self.key_df = None

    def get_file(self):
        return self.key_path

    def set_file(self, file):
        self.key_path = file

    def subject_to_key(self, subject: BidsSubject):
        if self.key_path == '':
            return ''

        if self.key_df is None:
            self.key_df = pd.read_csv(self.key_path)

        row = self.key_df.loc[self.key_df['id'] == subject.get_first_name() + ' ' + subject.get_last_name()]
        return row.iloc[0]['key'] if not row.empty else ''


