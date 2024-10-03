import re

# Reemplazar todos los espacios en blanco por guiones bajos (_):

texto = "Este es un ejemplo de texto con espacios"

p = re.compile(r'\s+')
print(re.sub(p , '_', texto))