from random import randint

count = 1

while count <= 3: 
	random_number = randint(1, 10)
	user_guess = int(input("Enter your guess: "))

	while user_guess < 1 or user_guess > 10:
		print("Invalid input. Enter a number from 1-10: ");
		user_guess = int(input("Enter your guess: "))

	print(f"random number = {random_number}")

	if random_number == user_guess:
		print("Your guess is correct!!!")
		break

	else:
		print("Your guess is wrong!!!")

	print()

	if count == 3:
		print("You lost the game!!!!")

	count += 1