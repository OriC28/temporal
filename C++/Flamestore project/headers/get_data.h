#include<iostream> //****TO USE CIN, COUT, GETLINE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<sstream> //*** TO USE STRINGSTREAM CLASS
#include<fstream> //** TO USE IFSTREAM CLASS
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
#include <windows.h>
using namespace std;

void print_data_in_out(string);
void get_header();
void print_data(vector<string>, vector<string>, vector<string>, vector<string>);

void get_dataCSV(vector<string> &ids, vector<string> &names, vector<string> &prices, vector<string> &amounts){
	string line;
	string id, name, price, amount;
	char delimiter = ';';
	ifstream file("./csv/products.csv");
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

void get_products_in_out(vector<string> &ids, vector<string> &names, vector<string> &prices, vector<string> &i_amounts,
						vector<string> &e_amounts, vector<string> &t_amounts, vector<string> &dates, string filename){

	string line;
	string id, name, price, i_amount, e_amount, t_amount, date;
	char delimiter = ';';
	ifstream file(filename);
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
			getline(stream, i_amount, delimiter);
			i_amounts.push_back(i_amount);
			getline(stream, e_amount, delimiter);
			e_amounts.push_back(e_amount);
			getline(stream, t_amount, delimiter);
			t_amounts.push_back(t_amount);
			getline(stream, date, delimiter);
			dates.push_back(date);

		}
		file.close();
	}else{
		cerr<<"\nError. Can't get the product.\n";
	}
}

void print_data_in_out(string filename){
	cout<<setfill('_')<<right<<setw(165)<<"\t"<<endl; //SEPERATOR

	cout<<"\t"<<
	setfill(' ')<<left<<setw(15)<<"#"<<
	setfill(' ')<<left<<setw(50)<<"Name"<<
	setfill(' ')<<left<<setw(10)<<"Price"<<
	setfill(' ')<<left<<setw(20)<<"Amount Initial"<<
	setfill(' ')<<left<<setw(20)<<"Amount Entered"<<
	setfill(' ')<<left<<setw(20)<<"Amount Total"<<
	setfill(' ')<<left<<setw(20)<<"Date"<<endl;

	cout<<setfill('_')<<right<<setw(165)<<"\t"<<endl;  //SEPERATOR



	vector<string> ids, names, prices, i_amounts, e_amounts, t_amounts, dates;
	get_products_in_out(ids, names, prices, i_amounts, e_amounts, t_amounts, dates, filename);
	for(int i=0; i<ids.size(); i++){
		cout<<"\t"<<
			setfill(' ')<<left<<setw(15)<<ids[i]<<
			setfill(' ')<<left<<setw(50)<<names[i]<<
			setfill(' ')<<left<<setw(10)<<prices[i]<<
			setfill(' ')<<left<<setw(20)<<i_amounts[i]<<
			setfill(' ')<<left<<setw(20)<<e_amounts[i]<<
			setfill(' ')<<left<<setw(20)<<t_amounts[i]<<
			setfill(' ')<<left<<setw(20)<<dates[i]<<endl;

			cout<<setfill('-')<<right<<setw(165)<<"\t"<<endl; //SEPERATOR
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

