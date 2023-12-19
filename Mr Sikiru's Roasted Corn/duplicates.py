def check_duplicates(list_of_strings):
	seen = set()
	duplicates = set()

	for items in list_of_strings:
		if items in seen:
			duplicates.add(items)
		else:
			seen.add(items)

	if duplicates:
		return list(duplicates)
	else:
		return "no duplicates"