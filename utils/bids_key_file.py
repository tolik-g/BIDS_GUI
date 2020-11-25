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

    def validate(self):
        if self.key_path == '':
            return False
        if self.key_df is None:
            self.key_df = pd.read_csv(self.key_path)
        return True

    def subject_to_key(self, subject: BidsSubject):
        if not self.validate():
            return ''

        row = self.key_df.loc[self.key_df['id'] == subject.get_first_name() + ' ' + subject.get_last_name()]
        return row.iloc[0]['key'] if not row.empty else ''

    def find_new_key(self):
        if not self.validate():
            return ''

        last_subject = self.key_df.iloc[-1]['key']
        last_number = int(last_subject.split('t')[1])
        return 'subject' + str(last_number + 1)

