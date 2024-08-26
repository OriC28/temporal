#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

bool get_data();
bool read_file(string, string);
string recover_password();

int main(){
	string password = recover_password();
	if (password!="") cout<<password;
	else cout<<"No password";
	return 0;
}

bool read_file(string user, string password){
	string line = "";
	vector <string> data;
	ifstream file("user.txt");

	//** looking archive user.txt

	if(!file.is_open()){
		cout<<"\nError. File not found or not readable.";
		exit(EXIT_FAILURE);
	}

	//** Adding data into vector

	while(file>>line){
		data.push_back(line);
	}

	//** Check username and password

	for(int i=0; i<data.size(); i++){
		if(user == data[i] && password == data[i+1]){
			return true;
		}
	}
	//file.close();
	return false;
}

bool get_data(){
	vector <string> data;
	string user, password;

	cout<<"Enter username: ";
	cin>>user;

	cout<<"Enter password: ";
	cin>>password;

	//Check existing data

	bool answer = read_file(user, password) ? true: false;
	return answer;
}

string recover_password(){
	vector<string> data;
	string line = "", password, user;

	cout<<"Enter username: ";
	cin>>user;

	ifstream file("user.txt");
	if(!file.is_open()){
		cout<<"\nError. File not found or not readable.";
		exit(EXIT_FAILURE);
	}
	while(file>>line){
		data.push_back(line);
	}

	for(int i=0; i<data.size(); i++){
		if(data[i] == user){
			password = data[i+1];
			break;
		}
	}

	return password;
}