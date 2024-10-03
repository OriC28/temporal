import re

# Comprobar si una cadena es un número de teléfono válido (formato: +34-123-456-7890)

texto = ["+34-123-456-7890", "34-123-456-7890", "+34-123-4567-890", "+341234567890"]

for i in texto:
	if re.findall(r"^.+\d{2}-\d{3}-\d{3}-\d{4}$", i):
		print("Es válido")
	else:
		print("No es válido")