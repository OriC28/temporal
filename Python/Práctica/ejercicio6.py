"""
Para resolver este desafío, debes escribir un algoritmo que elimine los elementos 
repetidos para obtener un conjunto único llamado champions.

Este algoritmo recibirá como entrada cuatro conjuntos de equipos, 
estos equipos serán de toda europa.
"""

teams = {"LIVERPOOL", "BAYER MUNICH", "ARSENAL", "JUVENTUS"}
italy = {"MILAN", "JUVENTUS"}
england = {"LIVERPOOL", "ARSENAL", "MANCHESTER UNITED"}
spain = {"REAL MADRID", "BARCELONA", "VALENCIA"}

def verificar_campeones(grupos):
	listado = []
	for i in grupos:
		listado.extend(list(i))
	
	for j in listado:
		if listado.count(j)>1:
			listado.remove(j)
	return set(listado)

def obtener_campeones(*args):
	champions = verificar_campeones([*args])
	print(champions)
	
obtener_campeones(teams, italy, england, spain)



