'''
Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que
sea más fácil disponer la condición que verifica que es una vocal.
'''
import re 

oracion = input("Ingrese una oración: ")

def verificar(oracion):
	vocales = 0
	for caracter in oracion:
		if re.findall(r'[aáeéiíoóuú]', caracter, re.IGNORECASE):
			vocales+=1
	if vocales!=0:
		print(f"La oración tiene {vocales} vocales.")
	else:
		print("La oración no tiene vocales.")

verificar(oracion)