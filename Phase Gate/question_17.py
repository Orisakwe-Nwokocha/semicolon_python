def squares_of_list():
	new_list = []
	for number in range(1, 26):
		new_list.append(number ** 2)
	
	return new_list

print(squares_of_list())