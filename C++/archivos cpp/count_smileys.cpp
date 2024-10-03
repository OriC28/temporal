#include<iostream>
#include<vector>
#include<regex>
using namespace std;

int count_smileys(vector<string> faces){
	int faces_found = 0;
	regex pattern("^[:;][-~]?[)D]$");
	for(auto& face : faces){
		(regex_match(face, pattern)) ? faces_found++ : faces_found;
	}
	return faces_found;
}

int main(int argc, char const *argv[]){
	cout<<count_smileys({";D", ":-(", ";~)", ":)", ";(", ";}", ":-D"});
	return 0;
}


