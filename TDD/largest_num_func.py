def largest_num(x, y, z):
	largest = 0

	if x > y and x > z:
		largest = x
	elif y > x and y > z:
		largest = y
	else:
		largest = z

	return f"{largest} is the largest number"

#print(largest_num(140, 20, 100))
	