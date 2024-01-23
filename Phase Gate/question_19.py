def prime_number(number):
	counter = 0
	for count in range(1, number + 1):
		if number % count == 0:
			counter += 1
	return counter == 2


print(prime_number(7))