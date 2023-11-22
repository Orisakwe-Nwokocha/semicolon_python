num = int(input("Enter a number:\n"))

if (num % 5 == 0 and num % 6 == 0):
	print("is",num, "divisible by 5 and 6? true")

else: 
	print("is",num, "divisible by 5 and 6? false")
	
if (num % 5 == 0 or num % 6 == 0):
	print("is",num, "divisible by 5 or 6? true")

else: 
	print("is",num, "divisible by 5 or 6? false")

if (num % 5 != 0 and num % 6 == 0) or (num % 5 == 0 and num % 6 != 0):
	print("is",num, "divisible by 5 or 6, but not both? true")

else: 
	print("is",num, "divisible by 5 or 6, but not both? false")

