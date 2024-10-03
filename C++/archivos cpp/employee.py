"""
Una empresa almacena los datos de N empleados, para esto,
en un proceso repetitivo se ingresa el sexo y el salario
de cada empleado. Se pide calcular:
a) La cantidad de personas que ganan más de 700 al mes.
b) El promedio de salarios.
c) El porcentaje de mujeres que trabajan en esa empresa
d) El porcentaje de varones que trabajan en esa empresa
"""

def main():
	revenue=0
	female = 0
	male = 0
	salaries = 0
	n = int(input("Which employee's quantity?: "))
	for i in range(n):
		sex = input("\nEnter employee's sex (male/female): ").lower()
		salary = float(input("\nEnter employee's salary: "))
		if (sex == "female" or sex == "male" and salary>0):
			salaries+=salary
			if salary>=700:
				revenue+=1
			if sex == "female":
				female+=1
			elif sex == "male":
				male+=1
		else:
			print("\n[DATA ISN'T CORRECT].")
	f = round(female/(female+male)*100, 2)
	m =  round(male/(female+male)*100, 2)
	salaries = round(salaries/(female + male), 2)
	print("\n\n-------------------------------------------------------------")
	print("Employees earning more than $700: ", revenue)
	print("Average salaries: " + str(salaries)+"$")
	print("Percentage of female working in that company: " + str(f) + "%")
	print("Percentage of male working in that company: " + str(m) + "%")
	print("-----------------------------------------------------------------")

if __name__ == '__main__':
	main()