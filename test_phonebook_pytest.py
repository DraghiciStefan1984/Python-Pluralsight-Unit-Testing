from phonebook import Phonebook
import pytest

def test_add_lookup_entry():
    phonebook=Phonebook()
    phonebook.add('Bob', '123')
    assert '123'==phonebook.lookup('Bob')

def test_phonebook_gives_access_to_names_and_numbers():
    phonebook=Phonebook()
    phonebook.add('Alice', '1234')
    phonebook.add('Bob', '5678')
    assert set(phonebook.names())=={'Alice', 'Bob'}
    assert '1234' in phonebook.numbers()

def test_missing_entry_raises_KeyError():
    phonebook=Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup('missing')