num = 10
for numbers in range(10, 1, -1):
	num -= 1	
	for items in range(numbers):
		print(num, end=" ")
	print()
	
print()

for i in range(1, 10):
	print(str(i) * i)
	
print()
