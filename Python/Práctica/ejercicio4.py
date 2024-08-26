'''
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o 
"El número aleatorio el mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
'''

import random

num: int
num_max = 20
encontrado = False
num_aleatorio = random.choice(range(1, num_max + 1))
intentos = 0
while(encontrado!=True):
	num = int(input(f"Ingrese un número del 1 al {num_max}: "))

	if num == num_aleatorio:
		print("\n¡En hora buena, has adivinado el número!\n")
		encontrado = True
		print(f"Número de intentos: {intentos}\n")
	else:
		if num > num_aleatorio:
			print("\n¡Cuidado!. El número aleatorio es menor.\n")
			intentos+=1
		elif num < num_aleatorio:
			print("\n¡Cuidado!. El número aleatorio es mayor.\n")
			intentos+=1
		encontrado = False
