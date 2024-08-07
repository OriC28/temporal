import requests
import json

url = 'https://api.jikan.moe/v4/top/anime'

data = requests.get(url)

if data.status_code == 200:
	data = json.loads(data.content)
	print("{:<10} {:<60} {:<100}".format("#", "Título", "Episódios"))
	for i in data['data']:
		print("{:<10} {:<60} {:<100}".format(str(i['mal_id']), i['title'],str(i['episodes'])))
else:
	print("Ha ocurrido un error.")


	