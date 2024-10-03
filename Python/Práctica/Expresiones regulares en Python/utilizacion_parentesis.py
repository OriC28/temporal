import re


employees = [
             "-Guybrush Threepwood-654261-Calle Falsa 123-AXY764581-",
             "-Elaine Marley-359752-Avenida Siempreviva 742-BZU620873-",
             "-Griswold Sopabuena-987653-Avenida Los Robles 2311N-AXY365410-",
             "-Herman Toothrot-159354-31 Spooner Street-CPN495103-",
             "-Pirata LeChuck-456215-Apartamento 5A, Calle 81-BZU573040-",
             "-René Rottingham-321656-56B Mansiones Whitehavens-CPN938601-",
             "-Charles DeGoulash-789327-221B Baker Street-AXY784960-",
             "-Edward Van Helgen-BZU486930-456918-124 Conch Street, Pacific Ocean",
            ]

employees_sort = [
             "-Guybrush Threepwood-Tel654261-Calle Falsa 123-AXY764581-",
             "-Elaine Marley-Tel359752-Avenida Siempreviva 742-BZU620873-",
             "-Griswold Sopabuena-Tel987653-Avenida Los Robles 2311N-AXY365410-",
             "-Herman Toothrot-Tel159354-31 Spooner Street-CPN495103-",
             "-Pirata LeChuck-Tel456215-Apartamento 5A, Calle 81-BZU573040-",
             "-René Rottingham-CPN938601-Tel321656-56B Mansiones Whitehavens^-",
             "-Charles DeGoulash-Tel789327-221B Baker Street-AXY784960-",
             "-Edward Van Helgen-BZU486930-Tel456918-124 Conch Street, Pacific Ocean",
            ]

# '()' trim specified text

print("\n---------------------------------------------------------------------------------------\n")
for employee in employees:
	num_departament = re.findall(r'-(\D{3})\d{6}', employee)
	print(num_departament)
print("\n---------------------------------------------------------------------------------------\n")

for employee in employees_sort:
	#num_departament = re.findall(r'-(\D{3})\d{6}', employee)
	num_departament = re.findall(r'-([^Tel]{3})\d{6}', employee)
	print(num_departament)
print("\n---------------------------------------------------------------------------------------\n")
