
def lower_function(string):
	new_string = ""
	letters_lower = "abcdefghijklmnñopqrstuvwxyz"
	letters_upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	for i in range(len(string)):
		if string[i] in letters_upper:
			new_string+=letters_lower[letters_upper.find(string[i])]
		else:
			new_string+=string[i]

	return new_string

lower_function("HOLA QUE tal")