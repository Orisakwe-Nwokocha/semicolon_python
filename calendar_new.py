month = int(input("Enter a month:\n"))
while (month < 1 or month > 12):
	month = int(input("Enter a number from 1-12:\n"))
year = int(input("Enter a year:\n"))
	
if (month == 1): 
	print("January", year, "had 3 days.")
        
if (month == 2 and year % 4 == 0): 
	print("February", year, "had 29 days.")

elif (month == 2):
	print("February", year, "had 28 days.")
      
if (month == 3): 
	print("March", year, "had 31 days.")
        	
if (month == 4): 
	print("April", year, "had 30 days.")
        	
if (month == 5): 
	print("May", year, "had 31 days.")
		
if (month == 6): 
	print("June", year, "had 30 days.")
		
if (month == 7): 
	print("July", year, "had 31 days.")
		
if (month == 8): 
	print("August", year, "had 31 days.")
		        
if (month == 9): 
	print("September", year, "had 30 days.")
		        
if (month == 10): 
	print("October", year, "had 31 days.")
	
if (month == 11): 
	print("November", year, "had 30 days.")

if (month == 12): 
	print("December", year, "had 31 days.")