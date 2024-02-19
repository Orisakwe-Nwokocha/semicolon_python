import pytest

from phonebook import Phonebook


@pytest.fixture
def nokia_phonebook():
    return Phonebook()


def test_that_phone_book_can_add_contact(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0

    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1


def test_that_phone_book_can_delete_contact(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0

    nokia_phonebook.add_contact("Orisha", "08035729982")
    nokia_phonebook.add_contact("Ajiri", "1234")
    nokia_phonebook.add_contact("Izu", "878")
    assert len(nokia_phonebook.get_contacts()) == 3

    nokia_phonebook.delete_contact("Ajiri", "1234")
    assert len(nokia_phonebook.get_contacts()) == 2


def test_search_for_an_existing_contact(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1

    assert nokia_phonebook.search_contact("Orisha") == "Orisha:\n08035729982\n"


def test_search_for_a_nonexistent_contact(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1

    assert nokia_phonebook.search_contact("Izu") == "No results for \"Izu\""


def test_phone_book_is_not_empty_view_contacts(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    nokia_phonebook.add_contact("Ajiri", "1234")
    assert len(nokia_phonebook.get_contacts()) == 2

    assert nokia_phonebook.view_contacts() == "Ajiri:\n1234\n\nOrisha:\n08035729982\n\n"


def test_phone_book_is_empty_view_contacts(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0

    assert nokia_phonebook.view_contacts() == "Phonebook is empty"


def test_edit_one_contact_info_only_contact_name_is_edited(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1
    assert nokia_phonebook.search_contact("Orisakwe Nwokocha") == "No results for \"Orisakwe Nwokocha\""

    nokia_phonebook.edit_contact("Orisha", "Orisakwe Nwokocha",
                                 "08035729982", "08035729982")
    assert nokia_phonebook.search_contact("Orisakwe Nwokocha") == "Orisakwe Nwokocha:\n08035729982\n"


def test_edit_one_contact_info_only_phone_number_is_edited(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1
    assert nokia_phonebook.search_contact("Orisha") != "Orisha:\n08125358910\n"

    nokia_phonebook.edit_contact("Orisha", "Orisha", "08035729982",
                                 "08125358910")
    assert nokia_phonebook.search_contact("Orisha") == "Orisha:\n08125358910\n"


def test_edit_all_contact_info_all_info_are_edited(nokia_phonebook):
    assert len(nokia_phonebook.get_contacts()) == 0
    nokia_phonebook.add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook.get_contacts()) == 1
    assert nokia_phonebook.search_contact("Orisha") != "Orisakwe Nwokocha:\n08125358910\n"

    nokia_phonebook.edit_contact("Orisha", "Orisakwe Nwokocha",
                                 "08035729982", "08125358910")
    assert nokia_phonebook.search_contact("Orisakwe Nwokocha") == "Orisakwe Nwokocha:\n08125358910\n"
