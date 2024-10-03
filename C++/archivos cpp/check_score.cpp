#include<iostream>
#include<unordered_map>
using namespace std;
#define r 3
#define c 1

int check_score(string (&symbols)[r][c]){
	int sum = 0;
	unordered_map<string, string> characters = {
		{"#","5"}, {"O","3"}, {"X","1"}, {"!","-1"}, {"!!","-3"}, {"!!!","-5"}
	};
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			for(auto& l: characters){
				if (symbols[i][j] == l.first){
					sum += stoi(l.second);
				} 
			}
		}
	}
	int result = (sum>0) ? sum : 0;
	return result;
}


int main(int argc, char const *argv[]){
	string symbols[r][c] = {{"#"},{"X"},{"O"}
	};
	cout<<check_score(symbols);

	return 0;
}