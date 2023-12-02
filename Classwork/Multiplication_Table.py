for numbers in range(1, 13):
	for items in range(1, 13):
		result = numbers * items
		print(f"{items:<2} * {numbers:<2} = {result:>4}", end="\t")
	print()
		