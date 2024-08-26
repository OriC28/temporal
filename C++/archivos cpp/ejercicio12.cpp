#include<iostream>
#include<cmath>
using namespace std;

int  solutions(int, int, int);

int main(){
	int a = 0, b=0, c=1;
	cout<<solutions(1, 0, 1);
	return 0;
}

int solutions(int a, int b, int c){
	int increment = (pow(b, 2) - 4*a*c);
	if (a !=0){
		if(increment>0) return 2;
		else if(increment == 0) return 1;
		else return 0;
	}
}