#include<iostream>
#include<fstream>
#include<locale.h>
#include<sstream> //*** TO USE CLASS STRINGSTREAM
#include <vector>
#include<windows.h>
using namespace std;

void create_web();
void open_website();

int main(){
	//create_web();
	open_website();
	return 0;
}

void get_dataCSV(vector<string> &ids, vector<string> &names, vector<string> &prices, vector<string> &amounts){
	string id, name, amount, price;
	string filename = "products.csv", line;
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
			getline(stream, amount, delimiter);
			amounts.push_back(amount);		
		}
	
		file.close();
	}else{
		cerr<<"Error. Can't get the product.";
	}
}

void create_web(){
	vector<string> ids, names, prices, amounts;
	ofstream web("index.html");
	web<<"<html>"<<endl;
		web<<"<head>"<<endl;
			web<<"<link rel=\"stylesheet\" href=\"style.css\">"<<endl;
		web<<"<head/>"<<endl;
		web<<"<body>"<<endl;

			//*************************** TABLE ******************************

			web<<"<table>"<<endl;

				//*********************** HEADER *****************************
				web<<"<tr>"<<endl;
					web<<"<th># ID<th/>"<<endl;
					web<<"<th>NAME<th/>"<<endl;
					web<<"<th>PRICE<th/>"<<endl;
					web<<"<th>AMOUNT<th/>"<<endl;
				web<<"<tr/>"<<endl;

				//********************** ROWS ********************************
				get_dataCSV(ids, names, prices, amounts);
				for(int i=0; i<ids.size(); i++){
					web<<"<tr>"<<endl;
                        web<<"<td>"<<ids[i]<<"<td/>"<<endl;
                        web<<"<td>"<<names[i]<<"<td/>"<<endl;
                        web<<"<td>"<<prices[i]<<"<td/>"<<endl;
                        web<<"<td>"<<amounts[i]<<"<td/>"<<endl;
                    web<<"<tr/>"<<endl;
				}

			web<<"<table/>"<<endl;
		web<<"<body/>"<<endl;
	web<<"<html/>"<<endl;
	web.close();
}

void open_website(){
	create_web();
	ShellExecute(GetDesktopWindow(),"open", "index.html", NULL, NULL, SW_SHOWNORMAL); 
}
