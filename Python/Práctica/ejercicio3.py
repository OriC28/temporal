'''
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena
de caracteres. Controlar que el string ingresado tenga entre 10 y 20
caracteres para que sea válido, en caso contrario mostrar un mensaje de error.
'''

clave = input("Ingrese una clave: ")


def validar(clave):
	size = len(clave)
	if size>=10 and size<=20: 
		print("Sí")
	else:
		print("No")

validar(clave)
