#include<iostream>
#include<string>
using namespace std;

//Last Digit Ultimate: Your job is to create a function, that takes
//3 numbers: a, b, c and returns true if the last digit of a * b = the last digit of c.

bool lastDig(int, int, int);

int main(){
	cout<<lastDig(55, 226, 5190);
	return 0;
}

bool lastDig(int num1 , int num2, int num3){
	int a = abs(num1%10), b = abs(num2%10), c = abs(num3%10), d = a*b;
	bool result = (d==c || abs(d%10)==c) ? true : false;
	return result;
}