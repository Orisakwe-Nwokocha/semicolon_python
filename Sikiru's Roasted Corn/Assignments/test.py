def menu():
	print("1. phonebook\n2. messages")
	menu2 = int(input("select option: "))
	if menu2 == 1:
		return phonebook()
def phonebook():
	print("1. search\n2. service nos")
	phonebook_menu = int(input("select option: "))
	if phonebook_menu == 2:
		return service_nos()
def options():
	print("1. Type of view\n2. Memory status")
	options2 = int(input("select option: "))
	if options2 == 1:
		return type_of_view()
def type_of_view():
	print("Type of view")
	type = int(input("enter 0 to go back: "))
	if type == 0:
		return menu()
def memory_status():
	print("Memory Status")
	memory = int(input("enter 0 to go back: "))
	if memory == 0:
		return menu()

menu()	
	
	
	