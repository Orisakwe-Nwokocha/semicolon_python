print("The numbers divisible by 7 and a multiple of 5 are:")
for numbers in range(1500, 2701):
	if numbers % 7 == 0 and numbers % 5 == 0:
		print(numbers)