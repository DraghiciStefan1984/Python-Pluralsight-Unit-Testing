import os


class Phonebook:
    def __init__(self, cache_dir):
        self.entries={}
        self.file_name='phonebook.txt'
        self.file_cache=open(os.path.join(str(cache_dir), self.file_name), 'w')

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

    def clear(self):
        self.entries={}
        self.file_cache.close()
        os.remove(self.file_name)