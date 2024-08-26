#include<iostream>
#include <algorithm>
using namespace std;

//Maskify the String: La tarea consiste en crear una función que tome una cadena,
//transforme todos los caracteres en "#" excepto los últimos cuatro y devuelva la nueva cadena enmascarada.

string maskify(string);


int main(){
	string text;
	//cout<<"Enter a password: ";
	//cin>>text;
	cout<<"Resultado --> "<<maskify("");
	return 0;
}

string maskify(string text){
	string hide, last_nums, result;
	int size = text.length();
	for(int i=4; i<size; i++){
		hide+="#";
	}
	for(int i=1; i<5; i++){
		last_nums+=text[size-i];
	}
	
	reverse(last_nums.begin(), last_nums.end());
	result = (size>4) ? hide + last_nums : text;
	return result;
}