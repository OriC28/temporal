import re


text = [
			'1 - La primera pregunta pide crear una función para encontrar el',
			'2 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'3 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'4 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'5 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'6 - cómo crear, actualizar, obtener y eliminar usuarios en Django'
		]


# '\s....letter\s' search into phrases the words that contain 4 characters (...o) and ends with 'o'
print("\n---------------------------------------------------------------------------------------\n")
for phrase in text:
	if re.findall(r'\s....o\s', phrase):
		print(phrase)

# '+' search one or more repetitions
print("\n---------------------------------------------------------------------------------------\n")
for phrase in text:
	if re.findall('(ta)+', phrase):
		print(phrase)

print("\n---------------------------------------------------------------------------------------\n")
for phrase in text:
	if re.findall(r'\s.*(ké)+.*\s', phrase):
		print(phrase)
print("\n---------------------------------------------------------------------------------------\n")
