import requests as rq
import json

# Consumir la API de Pokémon y obtener información sobre tipos
info = 'pokemon'
url = 'https://pokeapi.co/api/v2/{}/'.format(info)

def get_data(url, word=''):
	try:
		response = rq.get(url)
		data = json.loads(response.content.decode("utf-8"))["results"]
		print(f"{info}\n".capitalize())
		if response.status_code == 200:
			k = 0
			for i in data:
				if i['name'].startswith(word):
					print(f"{k+1} - {i['name'].capitalize()}")
					k+=1
	except Exception as e:
		print("Ocurrió un problema.", e)

get_data(url)