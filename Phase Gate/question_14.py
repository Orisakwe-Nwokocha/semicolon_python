def sum_of_odd_numbers():
	sum = 0
	for count in range(1, 51):
		if count % 2 != 0:
			sum += count
	return sum

print(sum_of_odd_numbers())