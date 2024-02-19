sum = 0
count = 0
num = int(input("Enter numbers (input 0 to end): "))
while num != 0:
	sum += num
	count += 1
	num = int(input("Enter numbers (input 0 to end): "))
average = sum / count
print(f"\nTotal number of imputs is {count}")
print(f"The sum of the numbers is {sum}") 
print(f"The average is {average}")