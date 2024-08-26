#include<iostream>
using namespace std;

//Triangular Number Sequence:Esta secuencia numérica triangular se genera a partir
//de un patrón de puntos que forman un triángulo.

int triangle(int);

int main(){
	cout<<triangle(215);
	return 0;
}

int triangle(int num){
	int num_points = 0;
	for(int i=1; i<=num; i++){
		num_points+=i;
	}

	return num_points;
}

