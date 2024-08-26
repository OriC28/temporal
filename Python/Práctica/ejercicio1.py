'''
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
ingresaron. Tener en cuenta que un espacio en blanco es igual a " ",
en cambio una cadena vacía es ""
'''

oracion = input("Ingrese una oración: ")

def verificiar_espacios(oracion):
	verificiar_espacios = 0
	for caracter in oracion:
		if caracter == " ":
			espacios+=1
	return espacios

print(verificiar_espacios(oracion))