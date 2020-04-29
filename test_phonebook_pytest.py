from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    phonebook=Phonebook(tmpdir)
    return phonebook

def test_add_lookup_entry(phonebook):
    phonebook.add('Bob', '123')
    assert '123'==phonebook.lookup('Bob')

def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add('Alice', '1234')
    phonebook.add('Bob', '5678')
    assert set(phonebook.names())=={'Alice', 'Bob'}
    assert '1234' in phonebook.numbers()

def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')