from phonebook import *


def test_that_phone_book_can_add_contact():
    nokia_phonebook = get_contacts()
    assert len(nokia_phonebook) == 1

    add_contact("Orisha", "08035729982")
    assert len(nokia_phonebook) == 1


def test_that_phone_book_can_delete_contact():
    nokia_phonebook = get_contacts()
    assert len(nokia_phonebook) == 0

    add_contact("Orisha", "08035729982")
    add_contact("ajiri", "1234")
    add_contact("izu", "878")
    assert len(nokia_phonebook) == 3

    delete_contact("ajiri")
    assert len(nokia_phonebook) == 2


def test_that_phone_book_search_contact_contact_exists():
    add_contact("Orisha", "08035729982")
    assert len(get_contacts()) == 1

    assert search_contact("Orisha") == "Orisha:\n08035729982\n"


def test_that_phone_book_search_contact_contact_does_not_exist():
    add_contact("Orisha", "08035729982")
    assert len(get_contacts()) == 1

    assert search_contact("izu") == "No results for \"izu\""


def test_view_contacts():
    assert False


def test_edit_one_contact_info():
    assert False


def test_edit_all_contact_info():
    assert False
