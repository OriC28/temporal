# Condiciones

# Si la repeticion seguida de letras es igual a 3:
 	### Solución: cambiar o eliminar una letra
# Si la repeticion seguida de letras es mayor a 3 pero menor a 6:
	### Solucion: cambiar la letra del centro

def secuencia_repetidas(message):
	if not message:
		return []

	repetidas = []
	secuencia = message[0]

	for i in range(1, len(message)):
		if message[i] == message[i - 1]:
			secuencia += message[i]
		else:
			if len(secuencia)>=3 and len(secuencia)<=5:
				repetidas.append(secuencia)
			secuencia = message[i]

	if len(secuencia)>=3 and len(secuencia)<=5:
		repetidas.append(secuencia)

	return repetidas

def secuencias_invalidas(message):
	if not message:
		return []

	repetidas_invalidas = []
	secuencia = message[0]

	for i in range(1, len(message)):
		if message[i] == message[i - 1]:
			secuencia += message[i]
		else:
			if len(secuencia)>5:
				repetidas_invalidas.append(secuencia)
			secuencia = message[i]
	if len(secuencia)>5:
		repetidas_invalidas.append(secuencia)

	return repetidas_invalidas

