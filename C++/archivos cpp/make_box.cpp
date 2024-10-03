#include<iostream>
#include<vector>
using namespace std;

void make_box(int num){ //num = 3
	vector<string> box;
	string v, temp, spaces;
	// First Row
	for(int i=0; i<num; i++){
		v+='#';
	}
	box.push_back(v);
	temp = v;
	// Spaces between columns
	for(int i=0; i<num-2; i++){
		spaces+=" ";
	}
	// Two Columns
	for(int i=0; i<num-2; i++){	
		v = '#' + spaces + '#';
		box.push_back(v);
	}
	// Adding end row
	box.push_back(temp);

	// Showing the box
	for(auto& i: box){
		cout<<i<<endl;
	}
}


int main(int argc, char const *argv[]){
	make_box(30);
	return 0;
}