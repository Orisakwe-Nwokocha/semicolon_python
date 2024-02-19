even = 0
odd = 0
for numbers in range(1, 100):
	if numbers % 2 == 0:
		even += 1
	else:	
		odd += 1
print(f"The number of even numbers between 1 and 100 are: {even}")
print(f"The number of odd numbers between 1 and 100 are: {odd}")