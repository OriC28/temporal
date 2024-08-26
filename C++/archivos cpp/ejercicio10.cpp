#include<iostream>
#include <vector>
using namespace std;

//Eliminate Odd Numbers within an Array: Cree una función que tome una matriz de números y devuelva solo los valores pares.
//Devuelva todos los números pares en el orden en que se dieron.
//Todos los casos de prueba contienen números válidos que van del 1 al 3000.

vector <int> noOdds(vector <int>);


int main(){
	vector <int> numbers = {718, 991, 449, 644, 380, 440};
	vector <int> onlyOdds = noOdds(numbers);
	for(int i=0; i<onlyOdds.size(); i++){
		cout<<onlyOdds[i]<<" ";
	}
	return 0;
}

vector <int> noOdds(vector <int> numbers){
	vector <int> onlyOdds;
	for(int i=0; i<numbers.size(); i++){
		if(numbers[i] % 2 == 0){
			onlyOdds.push_back(numbers[i]);
		}
	}

	return onlyOdds;
}
