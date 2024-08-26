#include<iostream>
using namespace std;

//How Many Vowels?
//Cree una función que tome una cadena y devuelva el número (recuento) de vocales contenidas en ella.

int countVowels(string);

int main(){
	cout<<countVowels("Prediction");
	return 0;
}

int countVowels(string str){
	string vowels = "aeiou";
	int count = 0;
	for(int i=0; i<str.length(); i++){
		for(int j=0; j<vowels.length(); j++){
			if(str[i] == vowels[j]) count++;
		}
	}
	return count;
}