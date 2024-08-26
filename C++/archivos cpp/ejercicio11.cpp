#include<iostream>
#include<sstream>
#include<string>
using namespace std;


int countWords(string);

int main(){
	string word = "Just an example here move along";
	cout<<countWords(word);
	return 0;
}

int countWords(string word){
	string result;
	int count = 0;
	for(int i=0; i<word.length(); i++){
		if(word[i]==' '){
			count++;
		}
	}

	return count+1;
}
