num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))

largest = 0

if num1 > largest:
	largest = num1

if num2 > num1:
	largest = num2

if num3 > num1:
	largest = num3

print(f"{largest} is the largest number")