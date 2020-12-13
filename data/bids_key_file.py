import pandas as pd


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
            self.key_df.set_index('key')
        return True

    def get_subjects_names(self):
        return list(self.key_df['name'])

    def subject_to_key(self, subject_name: str):
        if not self.validate():
            return ''

        row = self.key_df.loc[self.key_df['name'].str.lower() == subject_name]
        return row.iloc[0]['key'] if not row.empty else ''

    # TODO: add get_name_list() funciton that returns a list of subject names

    def find_new_key(self):
        if not self.validate():
            return ''

        last_subject = self.key_df.iloc[-1]['key']
        last_number = int(last_subject.split('-')[1])
        return 'sub-' + str(last_number + 1)

    def create_new_key(self, subject_name: str):
        if not self.validate():
            return

        new_key = self.find_new_key()
        self.key_df.loc[new_key] = {'key': new_key, 'name': subject_name}
        self.key_df.to_csv(self.key_path, index=False)
