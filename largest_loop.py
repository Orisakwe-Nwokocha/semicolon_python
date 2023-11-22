num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))

arr = [num1, num2, num3]
largest = arr[0]
smallest = arr[0]

for items in arr:
	if items > largest:
		largest = items
	
	if items < smallest:
		smallest = items

print(f"{smallest} is the smallest number")
print(f"{largest} is the largest number")