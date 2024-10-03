def upper_function(string):
	new_string = ""
	letters_lower = "abcdefghijklmnñopqrstuvwxyz"
	letters_upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	for i in range(len(string)):
		if string[i] in letters_lower:
			new_string+=letters_upper[letters_lower.find(string[i])]
		else:
			new_string+=string[i]

	return new_string

print(upper_function("que paso"))