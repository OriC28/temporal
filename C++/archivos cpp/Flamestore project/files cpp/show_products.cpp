#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<fstream> //*** TO USE FSTREAM, OFSTREAM AND IFSTREAM OBJECT
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<sstream>
#include<iomanip>
using namespace std;

void get_products_saved();
void print_products();

int main(){
	get_products_saved();

	return 0;
}

void get_products_saved(){
	vector<string> id_data, name_data, amount_data, price_data;
	string id, name, amount, price;
	string filename = "products.csv", line;
	char delimiter = ';';
	ifstream file(filename);
	if(file.is_open()){
		getline(file, line);
		while(getline(file, line)){
			stringstream stream(line);
			getline(stream, id, delimiter);
			id_data.push_back(id);
			getline(stream, name, delimiter);
			name_data.push_back(name);
			getline(stream, price, delimiter);
			price_data.push_back(price);
			getline(stream, amount, delimiter);
			amount_data.push_back(amount);		
		}
	
		file.close();
	}
	else{
		cout<<"The file can't open.";
	}
	//###### HEADER 

	cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR

	cout<<"\t"<<
	setfill(' ')<<left<<setw(15)<<"#"<<
	setfill(' ')<<left<<setw(50)<<"Name"<<
	setfill(' ')<<left<<setw(10)<<"Price"<<
	setfill(' ')<<left<<setw(20)<<"Amount"<<endl;

	cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl;  //SEPERATOR
	
	//###### DATA INTO products.csv

	for(int i=0; i<id_data.size(); i++){
		cout<<"\t"<<
			setfill(' ')<<left<<setw(15)<<id_data[i]<<
			setfill(' ')<<left<<setw(50)<<name_data[i]<<
			setfill(' ')<<left<<setw(10)<<price_data[i]<<
			setfill(' ')<<left<<setw(20)<<amount_data[i]<<endl;

			cout<<setfill('-')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR
	}


}

