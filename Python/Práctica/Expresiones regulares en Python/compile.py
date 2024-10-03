import re
import time as tm
text = [
			'1 - La primera pregunta pide crear una función para encontrar el',
			'2 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'3 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'4 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'5 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'6 - cómo crear, actualizar, obtener y eliminar usuarios en Django',
			'7 - La primera pregunta pide crear una función para encontrar el',
			'8 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'9 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'10 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'11 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'12 - cómo crear, actualizar, obtener y eliminar usuarios en Django',
			'13 - La primera pregunta pide crear una función para encontrar el',
			'14 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'15 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'16 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'17 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'18 - cómo crear, actualizar, obtener y eliminar usuarios en Django',
			'19 - La primera pregunta pide crear una función para encontrar el',
			'20 - próximo número primo más cercano. La segunda pregunta pide consumir',
			'21 - la API de Pokémon y obtener información sobre tipos. La tercera pregunta',
			'22 - modifica la función anterior para devolver solo los Pokémon. La cuarta',
			'23 - pregunta filtra los Pokémon que comienzan con S. La quinta pregunta explica',
			'24 - cómo crear, actualizar, obtener y eliminar usuarios en Django'
		]


print("\t\t\t\tWithout .compile()\n")

t0 = tm.time()

for i in text:
	if re.findall(r'\s.*ké.*\s', i):
		print(i)

t1 = tm.time()

print("\nDuration: ", float(t1-t0))

print("\n---------------------------------------------------------------------------------------\n")

print("\t\t\t\tWith .compile()\n")

t00 = tm.time()

pattern = re.compile(r'\s.*ké.*\s')
for j in text:
	if pattern.findall(j):
		print(j)

t11 = tm.time()

print("\nDuration: ", float(t11-t00))




