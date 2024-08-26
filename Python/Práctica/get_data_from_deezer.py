import requests
import json
import re
from os import system

artista = input("Ingrese el artista: ")

option = input ('''
	1. Albums\n
	2. Songs\n
	''')

def get_url(artista):
	p = re.compile(r'\s+')
	name = re.sub(p , '-', artista)
	return f'https://api.deezer.com/search?q={name}'

def get_albums(artista):
	url = get_url(artista)
	request  = requests.get(url)
	system("cls")
	print(f"\nAquí tienes algunos álbumes de {artista}\n:")
	data = json.loads(request.content)
	for i, dato in enumerate(data['data']):
		print(f"{i+1} - {dato['album']['title']}")


def get_songs( artista):
	url = get_url(artista)
	request  = requests.get(url)
	system("cls")
	print(f"Aquí tienes algunas canciones de {artista}:\n")
	data = json.loads(request.content)
	for i, dato in enumerate(data['data']):
		print(f"{i+1} - {dato['title']}")

if option == "1":
	get_albums(artista)

elif option == "2":
	get_songs(artista)

else:
	print("\n Elige una opción inválida.")


