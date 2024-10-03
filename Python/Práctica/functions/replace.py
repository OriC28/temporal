def replace_function(string, item_sub, item):
	new_string = ""
	for i in string:
		if i == item_sub:
			new_string+=item
		else:
			new_string+=i

	return new_string

print(replace_function("hola", "h", "b"))