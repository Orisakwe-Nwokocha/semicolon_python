total = 0
for items in range(1, 21):
	num = int(input(f"Enter number {items}: "))
	total += num
	
print(total)

print()

total = 0
counter = 1

while counter <= 20:
	num = int(input(f"Enter number {counter}: "))
	total += num
	counter += 1

print(total)