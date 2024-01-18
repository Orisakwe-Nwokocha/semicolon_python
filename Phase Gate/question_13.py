def factorial(number):
	if number in (0, 1):
		return 1

	if number < 0:
		return "Invalid"

	for count in reversed(range(1, number)):
		number *= count

	return number

print(factorial(0))
print(factorial(1))
print(factorial(-4))
print(factorial(5))