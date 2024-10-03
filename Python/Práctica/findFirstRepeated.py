'''
En la fábrica de juguetes del Polo Norte, cada juguete
tiene un número de identificación único. Sin embargo,
debido a un error en la máquina de juguetes, algunos
números han sido asignados a más de un juguete.

Encuentre el primer número de identificación que se ha
repetido, ¡donde la segunda aparición tiene el índice
más pequeño! En otras palabras, si hay más de un número
repetido, debes devolver el número cuya segunda aparición
aparece primero en la lista. Si no hay números repetidos,
devuelve -1.

Ejemplo:

const giftIds = [2, 1, 3, 5, 3, 2]
const firstRepeatedId = findFirstRepeated(giftIds)
console.log(firstRepeatedId) // 3
// Even though 2 and 3 are repeated
// 3 appears second time first
'''

def find_first_repeated(array):
	total_steps = []
	repeated = []
	data = []
	step = 0
	for i in range(len(array)):
		if array.count(array[i])>1:
			data.append((array[i], i))
			repeated.append(array[i])

	if repeated==[]:
		return -1
	else:
		repeated = list(set(repeated))
		for i in sorted(data):
			for j in repeated:
				if i[0] == j:
					step = abs(step - i[1])
				else:
					if step!=0:
						total_steps.append(step)
						step = 0
		minus = list(zip(repeated,total_steps))[0][1]
		print(minus)
		item = 0
		for i in list(zip(repeated,total_steps)):
			if i[1]<=minus:
				minus = i[1]
				item = i[0]
		return item
print(find_first_repeated([2, 1, 3, 5, 2, 1]))


