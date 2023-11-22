num = int(input("Enter your age:\n"))

while (num < 0):
	num = int(input("Invalid input. Please enter a number >= 0:\n"))

converted = num * 365

print(converted)