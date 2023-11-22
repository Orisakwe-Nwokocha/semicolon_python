num1 = float(input("Enter first floating number:\n"))
num2 = float(input("Enter second floating number:\n"))
num3 = float(input("Enter third floating number:\n"))

if (num1 < num2 and num1 < num3) and (num2 < num3):
	print(num1, num2, num3)

if (num1 < num2 and num1 < num3) and (num3 < num2):
	print(num1, num3, num2)

if (num2 < num1 and num2 < num3) and (num1 < num3):
	print(num2, num1, num3)

if (num2 < num1 and num2 < num3) and (num3 < num1):
	print(num2, num3, num1)

if (num3 < num1 and num3 < num2) and (num1 < num2):
	print(num3, num1, num2)

if (num3 < num1 and num3 < num2) and (num2 < num1):
	print(num3, num2, num1)

