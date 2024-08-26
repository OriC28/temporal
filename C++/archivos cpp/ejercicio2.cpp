#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

//Count Syllables: Cree una función que cuente el número de sílabas que
//tiene una palabra. Cada sílaba está separada por un guión '-'.

int numberSyllables(string);

int main(){
	string word = "ca-sa-gn-dkda";
	cout<<numberSyllables(word);
	return 0;
}

int numberSyllables(string word){
	string result;
	stringstream input_stringstream(word);
	int count = 0;
	while(getline(input_stringstream, result, '-')){
		count++;
	}

	return count;
}
