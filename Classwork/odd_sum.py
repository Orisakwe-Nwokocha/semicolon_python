odd_sum = 0
for numbers in range(1000, 5001):
	if numbers % 2 != 0:
		odd_sum += numbers
print(f"The sum of odd numbers is {odd_sum:,}")     

print()

odd = 0
count = 1000

while count <= 5000:
	if count % 2 != 0:
		odd += count
	count += 1
print(f"The sum of odd numbers is {odd:,}")
                              