#include<iostream>
using namespace std;

//Alphabet Soup: Cree una función que tome una cadena y devuelva una cadena con sus letras en orden alfabético.

string alphabetSoup(string);

int main(){
	cout<<alphabetSoup("javascript");
	return 0;
}

string alphabetSoup(string str){
	for(int i=0; i<str.length(); i++){
		char a = str[i];
		char j = i-1;
			while(j>=0 && str[j]>a){
				str[j + 1] = str[j];
				j--;
			}
			str[j + 1] = a;
	}
	return str;
}