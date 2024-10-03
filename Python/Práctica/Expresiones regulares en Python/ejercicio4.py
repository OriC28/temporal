import re

# Encontrar palabras que comiencen con una letra mayúscula

texto = "La capital de Francia es París, y la de Italia es Roma"

p = re.compile(r'\W+')
data = p.split(texto)
for palabra in data:
	if re.findall(r'^[A-Z]', palabra):
		print(palabra)
