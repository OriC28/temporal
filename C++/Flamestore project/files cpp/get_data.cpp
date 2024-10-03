#include<iostream>
#include<vector>
#include<sstream>
#include<fstream>
using namespace std;


void get_header();
void print_data(vector<string>, vector<string>, vector<string>, vector<string>);

void get_dataCSV(vector<string> &ids, vector<string> &names, vector<string> &prices, vector<string> &amounts){
	string line;
	string id, name, price, amount;
	char delimiter = ';';
	ifstream file("products.csv");
	if(file.is_open()){
		getline(file, line);
		while(getline(file, line)){
			stringstream stream(line);
			getline(stream, id, delimiter);
			ids.push_back(id);
			getline(stream, name, delimiter);
			names.push_back(name);
			getline(stream, price, delimiter);
			prices.push_back(price);
			getline(stream, amount, delimiter);
			amounts.push_back(amount);

		}
		file.close();
	}else{
		cerr<<"\nError. Can't get the product.\n";
	}
}

void get_header(){
	cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR

	cout<<"\t"<<
	setfill(' ')<<left<<setw(15)<<"#"<<
	setfill(' ')<<left<<setw(50)<<"Name"<<
	setfill(' ')<<left<<setw(10)<<"Price"<<
	setfill(' ')<<left<<setw(20)<<"Amount"<<endl;

	cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl;  //SEPERATOR
}

void print_data(vector<string> ids, vector<string> names, vector<string> prices, vector<string> amounts){
	for(int i=0; i<ids.size(); i++){
		cout<<"\t"<<
			setfill(' ')<<left<<setw(15)<<ids[i]<<
			setfill(' ')<<left<<setw(50)<<names[i]<<
			setfill(' ')<<left<<setw(10)<<prices[i]<<
			setfill(' ')<<left<<setw(20)<<amounts[i]<<endl;

			cout<<setfill('-')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR
	}
}

