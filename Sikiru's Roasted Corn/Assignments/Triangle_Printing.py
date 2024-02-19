for numbers in range(1, 11):
	for items in range(numbers):
		print("*", end="")

	for s in range(1, 14 - numbers):
		print(end=" ")

	for items in range(1, 12 - numbers):
		print("*", end="")

	for s in range(11 - numbers, numbers + 12):
		print(end=" ")

	for items in range(1, 12 - numbers):
		print("*", end="")

	for c in range(1, 14 - numbers):
		print(end=" ")

	for items in range(numbers):
		print("*", end="")

	print()