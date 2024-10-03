import re

text = '''La primera pregunta pide crear una función para encontrar el
		próximo número primo más cercano. La segunda pregunta pide consumir
		la API de Pokémon y obtener información sobre tipos. La tercera pregunta
		modifica la función anterior para devolver solo los Pokémon. La cuarta
		pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica
		cómo crear, actualizar, obtener y eliminar usuarios en Django.'''

result = re.search('pregunta', text)
result_full = re.findall('pregunta', text)

if result:
	print("Search success.")
	# .search returns only the first pattern despite having multiple repetitions
	print(f"Search using search method: {result}")
	# .findall returns all repetitions
	print(f"Search using findall method: {result_full}")

else:
	print("Pattern not found.")