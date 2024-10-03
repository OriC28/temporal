#include<iostream>
#include<algorithm>
using namespace std;

int letter_distance(string word1, string word2){
	int distance = 0;
	int length_min = min(word1.length(), word2.length());
	for(int i=0; i<length_min; i++){
		distance += abs((int) word1[i] -  (int) word2[i]); 
	}
	distance += word1.length() - word2.length();
	return distance;
}	

int main(int argc, char const *argv[]){
	cout<<letter_distance("house", "fly");
	return 0;
}

