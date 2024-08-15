import re

# Dividir una cadena en palabras separadas por comas o espacios

texto = "manzana,pera,plátano uva melón"

p = re.compile(r'[\s+,]')
frutas = re.sub(p , ',', texto).split(",")

for i, fruta in enumerate(frutas):
	print(f"\t{i+1} --- {fruta}\n")