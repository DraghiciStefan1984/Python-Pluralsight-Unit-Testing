import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook=Phonebook()

    def tearDown(self):
        self.phonebook=None

    def test_lookup_entry_by_name(self):
        self.phonebook.add('Bob', '12345')
        self.assertEqual('12345', self.phonebook.lookup('Bob'))

    def test_missing_enrty_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip('example not good')
    def test_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Bob', '123')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Sue', '456')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Mary', '123')
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add('Charlie', '456')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_normal_entries_is_consistent(self):
        self.phonebook.add('Bob', '123')
        self.phonebook.add('Sue', '456')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_duplicate_entries_is_inconsistent(self):
        self.phonebook.add('Bob', '123')
        self.phonebook.add('Sue', '123')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '123')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_add_names_and_numbers(self):
        self.phonebook('Bob', '123')
        self.assertIn('Bob', self.phonebook.get_names())
        self.assertIn('123', self.phonebook.get_phone_numbers())
