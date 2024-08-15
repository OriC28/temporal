import re

text = [
			'1 - La primera pregunta pide crear una función para encontrar el',
			'2 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'3 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'4 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'5 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'6 - cómo crear, actualizar, obtener y eliminar usuarios en Django'
		]


text2 = [
			'La primera pregunta pide crear una función para encontrar el',
			'próximo número primo más cercano. La segunda pregunta pide consumir',
			'la API de Pokémon y obtener información sobre tipos. La tercera preguntapm',
			'modifica la función anterior para devolver solo los Pokémon. La cuartaam',
			'pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explicapm',
			'cómo crear, actualizar, obtener y eliminar usuarios en Django'
		]


# '[]' returns all sentences that contain any of the letters included within the square brackets

print("\n---------------------------------------------------------------------------------------\n")

for phrase in text:
	if re.search('[ákx]', phrase):
		print(phrase)
print("\n---------------------------------------------------------------------------------------\n")

# '[]' is used like a range too

for phrase in text:
	if re.search('[3-6]', phrase):
		print(phrase)
print("\n---------------------------------------------------------------------------------------\n")
		
# print the phrase starst with 'l' or 'm'
for phrase in text2:
	if re.search('^[lm]', phrase):
		print(phrase)
print("\n---------------------------------------------------------------------------------------\n")



# print the phrase starst with 'l' or 'm'
for phrase in text2:
	if re.search('[pmam]$', phrase):
		print(phrase)
print("\n---------------------------------------------------------------------------------------\n")


peats = ['Gato', 'Perro', 'Loros', 'Perros', 'Gata', 'Iguana', 'Conejos', 'Hamster']

contador = 0
for peat in peats:
	if re.search('Gat[ao]', peat):
		contador+=1

print(f"{contador} persons have a cat")
print("\n---------------------------------------------------------------------------------------\n")
