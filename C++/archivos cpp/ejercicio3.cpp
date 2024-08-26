#include<iostream>
#include<string>
using namespace std;

//Burrrrrrrp: Cree una función que devuelva la cadena "Burp" con la cantidad de
//"r" determinada por los parámetros de entrada de la función.

string longBurp(int);

int main(){
	cout<<longBurp(5);
	return 0;
}

string longBurp(int num){
	string add;
	if (num>=1){
		for(int i=0; i<num; i++){
			add+="r";
		}
		
	}else{
		return "Please enter a number bigger than " + to_string(num) + ".";
	}
	return "Bu" + add + "p";
}