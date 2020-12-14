class BidsSubject:
    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name.lower()

    def set_name(self, name):
        self.name = name.rstrip().lstrip()

    def validate_empty(self):
        return self.name != ''
# TODO remove if not needed after main has the subject from dataset_subject_chooser
