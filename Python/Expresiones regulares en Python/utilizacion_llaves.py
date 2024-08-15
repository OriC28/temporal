import re

#Departamento: 3 dígitos
#Teléfono: 6 dígitos
#Legajo: 4 a 5 dígitos


employees = [
			 "-Guybrush Threepwood-581-654261-Calle Falsa 123-76458-",
             "-Elaine Marley-582-359752-Avenida Siempreviva 742-60873-",
             "-Griswold Sopabuena-581-987653-Avenida Los Robles 2311N-6541-",
             "-Herman Toothrot-583-159354-31 Spooner Street-9510-",
             "-Pirata LeChuck-456215-Apartamento 5A, Calle 81-582-7304-",
             "-René Rottingham-581-321656-56B Mansiones Whitehavens-98601-",
             "-Charles DeGoulash-580-789327-221B Baker Street-7896-",
             "-Edward Van Helgen-48630-581-456918-124 Conch Street, Pacific Ocean"
			]

# /d receives a digit and searches among the texts for those that contain n number of digits together


# any text that containts 6 digits together will be taken here

for employee in employees:
	phones = re.findall(r'\d{6}', employee)
	print(phones)
print("\n---------------------------------------------------------------------------------------\n")

# any text that cantains 3 digits and is between "-" will be taken here

for employee in employees:
	departaments = re.findall(r'-\d{3}-', employee)
	print(departaments)
print("\n---------------------------------------------------------------------------------------\n")

# any text that contains 4 or 5 digits and is between "-" will be taken here

for employee in employees:
	legajos = re.findall(r'-\d{4,5}-', employee)
	print(legajos)
print("\n---------------------------------------------------------------------------------------\n")

# \D+ retuns only any non-numeric character.

for employee in employees:
	names = re.search(r'-\D+', employee)
	print(names.group())
print("\n---------------------------------------------------------------------------------------\n")