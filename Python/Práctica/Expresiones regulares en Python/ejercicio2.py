import re

# Extraer números de una cadena

texto = "La casa cuesta 250000 dólares y el coche 30000 dólares"

resultado = re.findall(r'\d+', texto)
print(f"En el texto se encuentran los siguientes números: {resultado[0]} y {resultado[1]}.")