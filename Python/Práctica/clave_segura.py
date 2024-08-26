'''
1.....Debe tener exactamente 20 caracteres.
2......Contiene al menos una letra minúscula, una letra mayúscula y un dígito.
3.....No contiene tres caracteres repetidos seguidos (por ejemplo, "... aaa..." 
	es débil, pero "... aa... a..." es fuerte, suponiendo que se cumplan las 
	otras condiciones).'''
import re
from algoritmo_repeticiones import secuencia_repetidas, secuencias_invalidas

message = "000000aaaBBBccccDDDDeeeee"

def validate(message):
	repeticiones = secuencia_repetidas(message)
	invalidas = secuencias_invalidas(message)
	changes = 0
	if len(message)>20:
		print(f"{len(message)} characters total {len(message)-20} characters need to be removed.")
		changes+=1
		if message.islower():
			print("Replace any character uppercase letter.")
			changes+=1
		if message.isupper():
			print("Replace any character lowercase letter.")
			changes+=1
		if not re.findall(r'\d', message):
			print("Replace any character onewith digit.")
			changes+=1
		if not re.findall(r'\D', message):
			changes+=1
		if repeticiones:
			for i in repeticiones:
				print(f"Replacing one of the middle characters in each of the {i}.")
				changes+=1
	else:
		print(f"{len(message)} characters total {20 - len(message)} characters need to be added.")
		changes+=1

	if invalidas:
			for j in invalidas:
				print(f"Replacing or removing {j}.")
				changes+=1

	return f"{changes} at least changes."

print(validate(message))