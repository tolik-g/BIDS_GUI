class BidsSubject:
    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name.lower()

    def set_name(self, name):
        self.name = name.rstrip().lstrip()

    def validate_empty(self):
        return self.name != ''
