#include<iostream>
#include<cstring>
using namespace std;

//Broken Bridge: Cree una función que valide si un puente es seguro
//para caminar (es decir, si no tiene huecos por los que caer).

bool isSafeBridge(string);

int main(){
	cout<<isSafeBridge("###### ");
	return 0;
}

bool isSafeBridge(string bridge){
	for(int i=0; i<bridge.length(); i++){
		if(bridge[i]==' ' || bridge[i]!='#'){
			return false;
		}
	}
	return true;
}