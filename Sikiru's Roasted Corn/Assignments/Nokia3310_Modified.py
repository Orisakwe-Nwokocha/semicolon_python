def menu():
	print("""
	Menu

1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Speed dials
10. Reminders
11. Clock
12. Profiles
13. SIM services""")

	print()
	menu_options = input("Select option: ")
	match menu_options:
		case "1":
			return phone_book()
		case "2":
			return messages()
		case "3":
			return chat()
		case "4":
			return call_register()
		case "5":
			return tones()
		case "6":
			return settings()
		case "7":
			return call_divert()
		case "8":
			return games()
		case "9":
			return speed_dials()
		case "10":
			return reminders()
		case "11":
			return clock()
		case "12":
			return profiles()
		case "13":
			return SIM_services()
		case _:
			return menu()			 
			

def phone_book():
	print()
	print("""
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags""")

	print()
	phonebook_menu = input("Select option or enter 0 to go back to menu: ")
	match phonebook_menu:
		case "0":
			return menu()
		case "1":
			return search() 
		case "2":
			return service_nos()
		case "3":
			return add_name()
		case "4":
			return erase()
		case "5":
			return edit()
		case "6":
			return assign_tone()
		case "7":
			return send_b'card()
		case "8":
			return options()
		case "9":
			return speed_dials()
		case "10":
			return voice_tags()
		case _:
			return menu()
def search():
	print()
	print("Search")
	print()
	search_menu = input("Select option || enter 0 to go back to the phonebook menu || enter 00 to go back to the main menu: ")
	match phonebook_menu:
		case "0":
			return menu()
		case "00":
			return search() 
		case _:
			return menu()









menu()