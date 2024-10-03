'''
Cree una función en la que deba suministrársele una cadena con únicamente letras y espacios.
En caso contrario la misma debe retornar 0.

En caso de una cadena válida, la función deberá determinar la posición de cada caracter de la
cadena en el abecedario (Empezando desde 0), luego restará la primera letra de la cadena con la
última letra de la misma, es decir: primera_letra - ultima_letra. (resultado 1).

Las posiciones de las letras restantes deberán sumarse. (resultado 2).

Por último, el resultado final se establecerá al sumar ambos resultados (resultado 1 + resultado 2) y
el mismo se multiplicará por el doble de la cantidad de espacios que la cadena contenga.

Ejemplo 1:

determine("hola") ---> 32

Explicación:

h -> 7
o -> 14
l -> 11
a -> 0

resultado1 = 7 - 0 -> 7
resultado2 = 14 + 11 -> 25

resultado_final = 7 + 25 -> 32

Ejemplo 2:

determine("hola que tal") ---> 160

Explicación:

h -> 7
o -> 14
l -> 11
a -> 0

q -> 16
u -> 20
e -> 4

t -> 19
a -> 0
l -> 11

resultado1 = 7 - 11 -> -4
resultado2 = 14 + 11 + 0 + 16 + 20 + 4 + 19 + 0 -> 84

[HAY 2 ESPACIOS, POR TANTO SE DEBE MULTIPLICAR EL RESULTADO FINAL POR EL DOBLE, O SEA 4].

resultado_final = -4 + 84 -> 80*4 = 320

------- NOTAS:

1. Tome en cuenta que las posiciones de las letras del abecedario deben empezar desde el 0.
2. La función no debe tomar en cuenta los espacios en el principio o final de la cadena. 
				Ejemplo: "hola  " [NO DEBE TOMAR LOS ESPACIOS DEL FINAL]
3. La cadena puede tener tanto letras minúsculas como mayúsculas.
4. La función debe retornar 0 en caso de cualquier símbolo especial, digito e incluso letras con acentos.
5. Recuerde que cada espacio en la cadena vale por 2 y este debería multiplicar el resultado final.
6. No se preocupe por la longitud de la cadena.
'''
import string
letters = str(string.ascii_lowercase)

def validate_characters(word):
	special_characters: bool
	for i in word.lower():
		if i in letters or i==" ":
			special_characters = False
		else:
			special_characters = True
			break
	return special_characters

def determinate(word):
	word = word.strip().lower()
	rest_letters = 0
	spaces = 0
	if not validate_characters(word):
		first_last_letters = letters.find(word[0]) - letters.find(word[-1])
		for i in word[1:len(word)-1]:
			if letters.find(i)!=-1:
				rest_letters+=letters.find(i)
				print(letters.find(i))
			else:
				spaces+=2
		return (first_last_letters + rest_letters)*spaces if spaces!=0 else first_last_letters + rest_letters
	else:
		return 0
	
print(determinate("hola que tal"))