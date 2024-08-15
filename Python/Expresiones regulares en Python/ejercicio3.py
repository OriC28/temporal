import re

# Verificar si una cadena es una fecha válida en formato dd/mm/yyyy

fecha = input("Ingrese una fecha: ")

resultado = re.findall(r'(\d{2}/\d{2}/\d{4}$)', fecha)
	
if resultado:
	print("La fecha ingresada es válida.")
else:
	print("La fecha ingresada es inválida.")