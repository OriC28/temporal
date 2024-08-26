#include<iostream>
#include <utility>
#include<vector>
using namespace std;

//Pair Management: Dado un par, devuelve su PRIMER valor y su SEGUNDO valor. {valor1, valor2}

vector<int> pairs(pair <int,int>);

int main(){
	pair<int, int> p(14,46);
	vector<int> data;
	data = pairs(p);
	for(int i=0; i<data.size(); i++){
		cout<<data[i]<<" ";
	}
	return 0;
}

vector<int> pairs(pair <int,int> p){
	vector<int> data;
	data.push_back(p.first);
	data.push_back(p.second);
	return data;
}