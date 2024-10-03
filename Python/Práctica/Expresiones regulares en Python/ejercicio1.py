import re

# Validar direcciones de correo electrónico

correos = ["usuario@example.com",
		"invalido.com",
		"nombre@dominio.org",
		"otro@ejemplo.net",
		"correoprueba@gmail.com"]

def validar_correo(correo):
	if re.search(r'\s*.*@.*.[com,net,org]$', correo):
		print("Correo válido")
	else:
		print("Correo no válido")

c = input("Ingrese un correo electrónico: ")
validar_correo(c)