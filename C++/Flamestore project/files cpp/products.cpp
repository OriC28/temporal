#include<iostream> //****TO USE CIN, COUT, GETLINE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<sstream> //*** TO USE STRINGSTREAM CLASS
#include<fstream> //** TO USE IFSTREAM CLASS
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
#include <string>
#include <ctime>
#include "get_data.h"
using namespace std;


string get_date();
bool update_data(int, string);
void products();

int main(){
	products();
	return 0;
}

string get_date(){
	auto t = time(nullptr);
	auto tm = *std::localtime(&t);

	ostringstream oss;
	oss<<put_time(&tm, "%d-%m-%Y %H:%M:%S");
	auto date = oss.str();

	return date;
}


bool update_data(int quantity, string id_product){
	bool found;
	string date = get_date();
	vector<string> ids, names, prices, amounts;

	get_dataCSV(ids, names, prices, amounts);

	for (int i = 0; i <ids.size(); i++) {
		if (id_product == ids[i]) {
			int current_amount = stoi(amounts[i]);
			int new_amount = current_amount + quantity;
			amounts[i] = to_string(new_amount);
			break;
		}
	}

	// *** Rewriting the updated data back to the CSV file
	ofstream file("./csv/products_entries.csv");
	if(file.is_open()) {
		file<<"#;Name;Price;Amount;Date\n"; 
		for (int i = 0; i<ids.size(); i++){
			if (id_product == ids[i]) {
				file<<ids[i]<<";"<<names[i]<<";"<<prices[i]<<";"<<amounts[i]<<";"<<date<<"\n";
				break;
			}
		}
		file.close();
		return true;
	}
	return false;
}


void products(){
	string id_product;
	bool exists = false;
	int quantity;
	vector<string> ids, names, prices, amounts;
	while(1){
		system("cls");
		get_dataCSV(ids, names, prices, amounts);

		get_header();

		print_data(ids, names, prices, amounts);

		cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl;

		cout<<"\nEnter the product ID: ";
		cin>>id_product;

		cout<<"\nEnter the quantity of the product to add: ";
		cin>>quantity;
		
		for(int i=0; i<ids.size(); i++){
			if(id_product == ids[i]){
				exists = true;
				break;
			}
		}

		if(exists && quantity>0){
			bool update = update_data(quantity, id_product);
			if(update){
				cout<<"\nThe new quantity of products has been added, check in 'Show products'.\n"; 
				break;
			}
			else {
				cout<<"\nError. File can't open.\n";
				system("pause");
				system("cls");
			}
		}else{
			cout<<"\nPlease, enter validated data.\n";
			system("pause");
			system("cls");
		}
	}
}

