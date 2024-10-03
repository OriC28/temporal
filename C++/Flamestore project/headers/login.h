#include<iostream> //****TO USE CIN, COUT
#include<fstream> //*** TO USE FSTREAM, OFSTREAM AND IFSTREAM OBJECT
#include<vector>  //*** TO USE VECTOR CLASS AND HIS METHODS
#include <conio.h> //*** TO USE _GENTCH FUNCTION
using namespace std;

bool get_data();
bool read_file(string, string);
string recover_password();
void hide_password(char[]);

bool read_file(string user, char password[30]){
	string line = "";
	vector <string> data;
	ifstream file("./user.txt");

	//** SEARCHING FILE user.txt
	if(!file.is_open()){
		cout<<"\nError. File not found or not readable.\n";
		exit(EXIT_FAILURE);
	}

	//** ADD DATA TO THE VECTOR TO MANIPULATE DATA
	while(file>>line){
		data.push_back(line);
	}

	//** CHECK USERNAME AND PASSWORD
	for(int i=0; i<data.size(); i++){
		if(user == data[i] && password == data[i+1]){
			return true;
		}
	}
	return false;
}

bool get_data(){
	vector <string> data;
	string user;
	char password[30];

	cout<<"Enter username: ";
	cin>>user;

	cout<<"Enter password: ";
	hide_password(password);

	//CHECK EXISTING DATA
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
		cout<<"\nError. File not found or not readable.\n";
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

void hide_password(char password[30]){
	char t;
    int i=0;
    while (1){
        t = _getch();

        //** IF ENTER IS PRESS IT
        if (t == 13){
            password[i] = '\0';
            break;
        }

        //** IF BACKSPACE IS PRESS IT
        else if (t == 8 && i>0){
            cout<<"\b \b";
            i--;
        }

        //** LIMIT OF PASSWORD (30)
        else if (i<29){
            cout<<'*';
            password[i] = t;
            i++;
        }
    }
}