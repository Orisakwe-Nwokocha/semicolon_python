def fibonacci(series_number):
	print(0, 1, end=" ")
	series = 1
	previous_sum = 0	
	temp = 0
	for number in range(series_number):
		temp = series
		series += previous_sum
		print(f"{series}", end=" ")
		previous_sum = temp


fibonacci(10)		