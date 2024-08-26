#include<iostream>
#include <unordered_map>
#include <string>
using namespace std;

void hacker_speak(string);

int main(){
	hacker_speak("Epale todo bien");
	return 0;
}

// a = 4, e = 3, i = 1, o = 0, s = 5

void hacker_speak(string str){
	unordered_map<char, char> letters = {
		{'a','4'}, {'e','3'},{'i','1'},{'o','0'},{'s','5'}
	};

	for (auto& letter : str){
		 for(const auto& it : letters){
			if (letter == it.first){
				letter = it.second;
			}
		}
	}

	cout<<str;
}