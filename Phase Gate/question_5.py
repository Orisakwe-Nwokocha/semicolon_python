def is_vowel_or_consonant(character):
	character = character.casefold()
	if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
		return "vowel"
	else:
		return "consonant"



print(is_vowel_or_consonant('b'))
print(is_vowel_or_consonant('U'))