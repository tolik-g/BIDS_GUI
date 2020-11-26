

class BidsSubject:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).lower()

    def validate_empty(self):
        return self.first_name != '' and self.last_name != ''

    def set_first_name(self, name):
        self.first_name = name.rstrip().lstrip()

    def set_last_name(self, name):
        self.last_name = name.rstrip().lstrip()
