#include<iostream>
#include<ctype.h>
using namespace std;

/*
Una empresa almacena los datos de N empleados, para esto,
en un proceso repetitivo se ingresa el sexo y el salario de
cada empleado. Se pide calcular:

a) La cantidad de personas que ganan más de 700 al mes.
b) El promedio de salarios.
c) El porcentaje de mujeres que trabajan en esa empresa
d) El porcentaje de varones que trabajan en esa empresa
*/

string lower_sex(string sex){
	for(auto& i : sex){
		i = tolower(i);
	}
	return sex;
}

int main(int argc, char const *argv[]){
	int n, salary, revenue=0, salaries=0;
	int female=0, male=0;
	string sex;
	cout<<"Enter the employee numbers: ";
	cin>>n;
	for(int i=0; i<n; i++){
		cout<<"\nEnter the sex (female / male): ";
		cin>>sex;
		cout<<"\nEnter the salary: ";
		cin>>salary;
		string lowercase_sex = lower_sex(sex);
		if(lowercase_sex=="female" || lowercase_sex=="male" && salary>0){
			salaries+=salary;
			if(salary>=700){
				revenue++;
			}
			if(lowercase_sex=="female"){
				female++;
			}
			else if(lowercase_sex == "male"){
				male++;
			}
		}
	}
	
	cout<<"\nEmployees earning more than $700: "<<revenue<<endl;
	cout<<"Average salaries: "<<salaries/(female+male)<<endl;
	cout<<"Percentage of female working in that company: "<<(female/(female+male))*100<<"%"<<endl;
	cout<<"Percentage of male working in that company: "<<(male/(female+male))*100<<"%"<<endl;
	return 0;
}