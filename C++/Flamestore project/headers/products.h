#include<iostream> //****TO USE CIN, COUT, GETLINE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<sstream> //*** TO USE STRINGSTREAM CLASS
#include<fstream> //** TO USE IFSTREAM CLASS
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
#include <string> //*** TO USE STOI FUNCTION
#include <ctime>
using namespace std;

string get_date();
bool update_data(int, string, string, string);
bool products(string);

string get_date(){
	auto t = time(nullptr);
	auto tm = *std::localtime(&t);

	ostringstream oss;
	oss<<put_time(&tm, "%d-%m-%Y %H:%M:%S");
	auto date = oss.str();

	return date;
}

bool update_data(int quantity, string id_product, string mode, string filename){
	string date = get_date();
	int current_amount;
	bool found;
	vector<string> ids, names, prices, amounts;

	get_dataCSV(ids, names, prices, amounts);
	for (int i = 0; i <ids.size(); i++) {
		if (id_product == ids[i]){
			current_amount = stoi(amounts[i]);
			if (mode == "input"){
				int new_amount = current_amount + quantity;
				amounts[i] = to_string(new_amount);
			}else if (mode == "output" && quantity<=current_amount){
				int new_amount = current_amount - quantity;
				amounts[i] = to_string(new_amount);
			}else{
				return false;
			}
			break;
		}
	}

	// *** Rewriting the updated data back to the CSV file
	ofstream file(filename, ios::app);
	if(file.is_open()){
		 //***  If file is empty, write the header
        file.seekp(0, std::ios::end); //*** Move cursor to the end
        if (file.tellp() == 0) { // *** If size file is 0 than file is empty
            file << "#;Name;Price;Initial amount;Amount entered;Amount total;Date\n";
        }
        //** Adding products
		for (int i = 0; i<ids.size(); i++){
			if (id_product == ids[i]){
				file<<ids[i]<<";"<<names[i]<<";"<<prices[i]<<";"<<current_amount<<";"<<quantity<<";"<<
					amounts[i]<<";"<<date<<"\n";
				break;
			}
		}
		file.close();
		// *** Update products.csv file than add entries
		ofstream file_update("./csv/products.csv");
		if(file_update.is_open()){
			file_update<<"#;Name;Price;Amount\n";
			for(int i=0; i<ids.size(); i++){
				file_update<<ids[i]<<";"<<names[i]<<";"<<prices[i]<<";"<<amounts[i]<<";"<<"\n";
			}
			file_update.close();
			return true;
		}
	}
	
	return false;
}

bool products(string mode){
	system("cls");
	string id_product, action;
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
		if(mode=="input"){
			action = "add";
			cout<<"\nEnter the quantity of the product to "<<action<<": ";
		}else{
			action = "reduce";
			cout<<"\nEnter the quantity of the product to "<<action<<": ";
		}
		cin>>quantity;
		
		for(int i=0; i<ids.size(); i++){
			if(id_product == ids[i]){
				exists = true;
				break;
			}
		}

		if(exists && quantity>0){
			bool update = (mode == "input") ? update_data(quantity, id_product, mode, "./csv/products_entries.csv") : update_data(quantity, id_product, mode, "./csv/products_outputs.csv");
			if(update) return true;
		}
		return false;
	}
}
