#include<iostream>
using namespace std;

int invert_num(int num){
	int value;
	string temp;
	string new_num = to_string(num%10) + to_string((num/10)%10) + to_string((num/10)/10);
	if(new_num.length() != to_string(num).length()){
		for(int i=0; i<to_string(num).length(); i++){
			temp+=new_num[i];
		}
		value = num-stoi(temp);
	}else{
		value = num - stoi(new_num);
	}
	int result =  (value>0) ? value : 0;
	return result;
}

int main(int argc, char const *argv[]){
	cout<<invert_num(832);
	return 0;
}