from operator import itemgetter


class Phonebook:
    def __init__(self):
        self.contacts = []

    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact_name: str, phone_number: str):
        contacts_dict = {"name": contact_name, "phone_number": phone_number}
        self.contacts.append(contacts_dict)

    def delete_contact(self, contact_name: str, phone_number: str):
        for contact in self.contacts:
            condition = contact["name"] == contact_name and contact["phone_number"] == phone_number
            if condition:
                self.contacts.remove(contact)
                break

    def search_contact(self, contact_name: str) -> str:
        contact_info = ""

        for contact in self.contacts:
            if contact["name"] == contact_name:
                contact_info += contact["name"] + ":\n" + contact["phone_number"] + "\n"

        if contact_info:
            return contact_info
        else:
            return f"No results for \"{contact_name}\""

    def view_contacts(self) -> str:
        all_contacts = ""

        for contact in sorted(self.contacts, key=itemgetter("name")):
            all_contacts += contact["name"] + ":\n" + contact["phone_number"] + "\n\n"

        if all_contacts:
            return all_contacts
        else:
            return "Phonebook is empty"

    def edit_contact(self, contact_name: str, new_name: str, phone_number: str, new_phone_number: str):
        for contact in self.contacts:
            condition = contact["name"] == contact_name and contact["phone_number"] == phone_number
            if condition:
                contact["name"] = new_name
                contact["phone_number"] = new_phone_number
            break
