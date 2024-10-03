import re

employees = [
             "-Guybrush Threepwood-Noviembre-Calle Falsa 123-AXY764581-",
             "-Elaine Marley-Diciembre-Avenida Siempreviva 742-BZU620873-",
             "-Griswold Sopabuena-Nov-Avenida Los Robles 2311N-AXY365410-",
             "-Herman Toothrot-Octubre-31 Spooner Street-CPN495103-",
             "-Pirata LeChuck-Enero-Apartamento 5A, Calle 81-BZU573040-",
             "-René Rottingham-Noviembre-56B Mansiones Whitehavens-CPN938601-",
             "-Charles DeGoulash-Agosto-221B Baker Street-AXY784960-",
             "-Edward Van Helgen-BZU486930-Nov-124 Conch Street, Pacific Ocean",
            ]

employees_sort = [
             "-Guybrush Threepwood-tel654261-Calle Falsa 123-AXY764581-",
             "-Elaine Marley-te:359752-Avenida Siempreviva 742-BZU620873-",
             "-Griswold Sopabuena-te:987653-Avenida Los Robles 2311N-AXY365410-",
             "-Herman Toothrot-159354-31 Spooner Street-CPN495103-",
             "-Pirata LeChuck-tel456215-Apartamento 5A, Calle 81-BZU573040-",
             "-René Rottingham-te:321656-56B Mansiones Whitehavens-CPN938601-",
             "-Charles DeGoulash-te:789327-221B Baker Street-AXY784960-",
             "-Edward Van Helgen-BZU486930-456918-124 Conch Street, Pacific Ocean"
            ]

print("\n---------------------------------------------------------------------------------------\n")
for employee in employees_sort:
	phone = re.findall(r'-(?:tel|te:)?(\d{6})-', employee)
	print(phone)

print("\n---------------------------------------------------------------------------------------\n")

for employee in employees:
	month = re.search(r'-Nov(iembre)?-', employee)
	if month:
		print(month.group())

print("\n---------------------------------------------------------------------------------------\n")