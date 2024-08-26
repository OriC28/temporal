#include<iostream>
#include<vector>
using namespace std;

//Sort Numbers in Ascending Order: Cree una función que tome una matriz de números
//y devuelva una nueva matriz, ordenada en orden ascendente (de menor a mayor).

//Ordene la matriz de números en orden ascendente.
//Si el argumento de la función es, una matriz vacía, o ; devuelve una matriz vacía. null, undefined
//Devuelve una nueva matriz de números ordenados.

vector<int> sortNumsAscending(vector<int>);
void writeArray();

int main(){
	//sortNumsAscending(numbers);
	writeArray();
	return 0;		
}

vector<int> sortNumsAscending(vector<int> arr){
	int size = arr.size();
	if (size>0){
		for(int i=1; i<size; i++){
			int a = arr[i];
			int j = i-1;

			while(j>=0 && arr[j]>a){
				arr[j + 1] = arr[j];
				j--;
			}
			arr[j + 1] = a;
		}
	}
	return arr;
}

void writeArray(){
	vector<int> numbers = {10,4,6,13,1,139};
	vector<int> arr = sortNumsAscending(numbers);
	for(int i=0; i<arr.size(); i++){
		cout<<arr[i]<<" ";
	}
}

