import phonebook
from phonebook import *

add_contact("orisha", "1234")
add_contact("orisha", "1234")
add_contact("ajiri", "1234")

print(get_contacts())

# delete_contact("ajiri")

print(search_contact("orish"))
print(view_contacts())

print(get_contacts())