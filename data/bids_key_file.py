import pandas as pd


class BidsKeyFile:
    def __init__(self):
        self.key_path = ''
        self.key_df = None

    def get_file(self):
        return self.key_path

    def set_file(self, file):
        self.key_path = file
        self.key_df = None

    def validate(self):
        if self.key_path == '':
            return False
        if self.key_df is None:
            self.key_df = pd.read_csv(self.key_path)
            self.key_df.set_index('key')
        return True

    def get_subjects_names(self):
        if not self.validate():
            return []
        return list(self.key_df['name'])

    def subject_to_key(self, subject_name: str):
        if not self.validate():
            return ''
        row = self.key_df.loc[self.key_df['name'] == subject_name]
        return row.iloc[0]['key'] if not row.empty else ''
