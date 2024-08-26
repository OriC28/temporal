#include<iostream>
#include<cmath>
using namespace std;

//A Circle and Two Squares: Cree una función que tome un número entero (radio del círculo)
//y devuelva la diferencia de las áreas de los dos cuadrados.

int squareAreasDifference(int);

int main(){
	cout<<squareAreasDifference(7);
	return 0;
}

int squareAreasDifference(int radio){
	return 2*pow((2*radio*sqrt(2)/2), 2) -pow((2*radio*sqrt(2)/2), 2) ;
}