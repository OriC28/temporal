#include<iostream>
using namespace std;

//Repeating Letters: Cree una función que tome una cadena y devuelva una cadena en
//la que cada carácter se repita una vez.

string doubleChar(string);

int main(){
	cout<<doubleChar("Hola Chamo");

	return 0;
}

string doubleChar(string word){
	string result;
	for(int i=0; i<word.length(); i++){
		for(int j=0; j<2; j++){
			result+=word[i];
		}
	}

	return result;
}