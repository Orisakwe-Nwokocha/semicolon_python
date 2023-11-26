print("The prime numbers between 1 and 100 (both inclusive) are:")
for items in range(1, 101):
	counter = 0
	for num in reversed(range(1, 101)):
		if items % num == 0:
			counter += 1		
	if counter == 2:
		print(items, end=" ")
	
	
	
