print("number\tsquare\tcube")


for items in range(0, 6):
	square = items ** 2
	cube = items ** 3
	print(items, square, cube, sep='\t')