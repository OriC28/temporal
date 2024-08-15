import re

text = [
			'La primera pregunta pide crear una función para encontrar el',
			'próximo número primo más cercano. La segunda pregunta pide consumir',
			'la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'cómo crear, actualizar, obtener y eliminar usuarios en Django'
		]


# '^' is used to search a phrase that starts with a specific pattern 

# '$' is used to search a phrase that ends with a specific pattern 

for phrase in text:
	if re.search('^La', phrase):
		print(phrase)
	if re.search('explica$', phrase):
		print(phrase)

