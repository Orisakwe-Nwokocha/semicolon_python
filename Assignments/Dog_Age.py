dog_age = int(input("Enter a number: "))

if dog_age < 1:
	print("Invalid input")
 
elif dog_age <= 2:
	human_year = dog_age * 10.5 
	print(f"The dog's age in dog years is {human_year}")
	
elif dog_age > 2:
	human_year = int(((dog_age - 2) * 4) + (2 * 10.5))
	print(f"The dog's age in dog years is {human_year}")