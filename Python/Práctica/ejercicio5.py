'''
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 5 elementos enteros aleatorios comprendidos entre 1 y 3.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 
mezclar la lista y volver a controlar hasta que haya un 1. 
3) Imprimir la lista.
'''

import random

def generar_listado():
	listado = []
	for i in range(5):
		listado.append(random.choice(range(1,4)))
	return listado

def listado_controlado():
	for i in range(5):
		listado = generar_listado()
		if listado[0] == 1:
			return listado
		else:
			listado = generar_listado()

print(listado_controlado())


