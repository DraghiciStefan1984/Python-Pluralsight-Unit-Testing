class Phonebook:
    def __init__(self):
        self.entries={}

    def add(self, name, phone_number):
        self.entries[name]=phone_number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def names(self):
        return self.entries.keys()

    def numbers(self):
        return self.entries.values()