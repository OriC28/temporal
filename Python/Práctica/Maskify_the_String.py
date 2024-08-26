#Maskify the String: La tarea consiste en crear una función que tome una cadena,
#transforme todos los caracteres en "#" excepto los últimos cuatro y devuelva la nueva cadena enmascarada.

string = input("Enter a password: ")
hide_nums = ""
for i in range(len(string)-4):
	hide_nums+='#'

result = hide_nums + string[len(string)-4:] if len(string)>4 or string=="" else string
print("Resultado -->", result)


