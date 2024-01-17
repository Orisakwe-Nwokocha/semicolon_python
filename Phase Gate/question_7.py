def day_of_the_week(number):
	match number:
		case 1:
			return "The day of the week is Sunday"
		case 2:
			return "The day of the week is Monday"
		case 3:
			return "The day of the week is Tuesday"
		case 4:
			return "The day of the week is Wednesday"
		case 5:
			return "The day of the week is Thursday"
		case 6:
			return "The day of the week is Friday"
		case 7:
			return "The day of the week is Saturday"
		case default:
			return "Not a valid input"


print(day_of_the_week(9))
print(day_of_the_week(4))