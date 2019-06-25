import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
	#part of the test fixture
	#setup the intial resources required by all the tests
	def setUp(self):
		self.phonebook=Phonebook()
	
	#part of the test fixture
	#remove the resources after all tests have run
	def tearDown(self):
		pass
		
	def test_lookup_entry_by_name(self):
		phonebook.add('Bob', '12345')
		self.assertEqual('12345', phonebook.lookup('Bob'))
		
	def test_missing_entry_raises_KeyError(self):
		with self.assertRaises(KeyError):
			phonebook.lookup('missing')
			
	@unittest.skip('Work in progress')
	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(phonebook.is_consistent())
		
	def test_phonebook_with_normal_entries_is_consistent(self):
		self.phonebook.add('Bob', '12345')
		self.phonebook.add('Mary', '678910')
		self.assertTrue(self.phonebook.is_consistent())
		
	def test_phonebook_with_normal_entries_is_inconsistent(self):
		self.phonebook.add('Bob', '12345')
		self.phonebook.add('Mary', '12345')
		self.assertFalse(self.phonebook.is_consistent())
		
	def test_phonebook_with_numbers_that_prefix_obe_another_is_inconsistent(self):
		self.phonebook.add('Bob', '12345')
		self.phonebook.add('Mary', '123')
		self.assertFalse(self.phonebook.is_consistent())
		
	def test_phonebook_adds_names_and_numbers(self):
		self.phonebook.add('Sue', '12345')
		self.assertIn('Sue', self.phonebook.get_names())
		self.assertIn('12345', self.phonebook.get_numbers())
		
#test
if __name__=='__main__':
	unittest.main()