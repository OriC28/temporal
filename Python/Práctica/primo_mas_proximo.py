
# Crear una función para encontrar el 
# próximo número primo más cercano

def es_primo(num):
	contador = 0
	for i in [x for x in range(2, num + 1)]:
		if num % i == 0: contador += 1
	if contador>1: return False
	return True

def proximo_primo_de(num):
	for i in range(2, 11):
		primo_prox = list(filter(es_primo, [x for x in range(num + 1, num + 10)]))[0]
		print(list(filter(es_primo, [x for x in range(num + 1, num + 10)])))
		return primo_prox

num = 45
print(f"El número primo más cercado de {num} es:", proximo_primo_de(num))
