
def strip_function(string):
	new_string = ""
	characters = list(string)
	while(characters[0] == " "):
		characters.remove(characters[0])
		while(characters[-1] == " "):
			characters.pop()

	for i in characters:
		new_string+=i
	
	return new_string

print(strip_function("   hola que tal")) 