from operator import itemgetter

contacts = []


def get_contacts():
    return contacts


def add_contact(contact_name: str, phone_number: str):
    contacts_dict = {"name": contact_name, "phone_number": phone_number}
    contacts.append(contacts_dict)



def delete_contact(contact_name: str):
    for contact in contacts:
        if contact["name"] == contact_name:
            contacts.remove(contact)


def search_contact(contact_name: str) -> str:
    contact_info = ""

    for contact in contacts:
        if contact["name"] == contact_name:
            contact_info += contact["name"] + ":\n" + contact["phone_number"] + "\n"

    if contact_info:
        return contact_info
    else:
        return f"No results for {contact_name}"


def view_contacts() -> str:

    all_contacts = ""

    for contact in sorted(contacts, key=itemgetter("name")):
        all_contacts += contact["name"] + ":\n" + contact["phone_number"] + "\n\n"

    if all_contacts:
        return all_contacts
    else:
        return "Phonebook is empty"


def edit_contact(contact_name: str, new_name: str):
    for contact in contacts:
        if contact["name"] == contact_name:
            contact["name"] = new_name


def edit_contact(contact_name: str, new_number: str):
# def edit_contact(contact_name: str, new_name: str, new_number: str):