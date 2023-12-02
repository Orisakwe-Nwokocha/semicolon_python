pass_count = 0
fail_count = 0

scores = float(input("Enter student scores (enter -1 to end input: ")) 

while scores != -1:
	if scores < -1:
		print("Invalid input")

	elif scores >= 0 and scores < 45:
		fail_count += 1

	elif scores >= 45 and scores <= 100:
		pass_count  += 1

	scores = float(input("Enter student scores (enter -1 to end input: "))

if pass_count != 0 or fail_count != 0:
	print(f"The number of students who passed = {pass_count}")
	print(f"The number of students who failed = {fail_count}")
else:
	print("No grades were entered")