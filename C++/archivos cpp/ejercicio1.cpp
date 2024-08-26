#include<iostream>
#include <vector>
using namespace std;

//Absolute Sum: Tome un array de números enteros (positivo o negativo o ambos)
//y devuelva la suma del valor absoluto de cada elemento.

int getAbsSum(vector <int>);
int main(){
	vector<int> array = {1,-5,-61,7};
	cout<<"Resultado: "<<getAbsSum(array);
	return 0;
}

int getAbsSum(vector <int> array){
	int sumaAbs = 0;
	for(int i=0; i<array.size(); i++){
		sumaAbs = (array[i]<0) ? sumaAbs + array[i]*(-1): sumaAbs + array[i];
	}
	return sumaAbs;
}