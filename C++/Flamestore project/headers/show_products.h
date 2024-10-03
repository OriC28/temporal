#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
using namespace std;

void get_products_saved();

void get_products_saved(){
	system("cls");
	vector<string> ids, names, prices, amounts;

	// ########## GET DATA INTO CSV FILE
	get_dataCSV(ids, names, prices, amounts); // get_dataCSV is defined into "get_data.h" included in main.cpp

	//###### HEADER 
	get_header();
	
	//###### DATA INTO products.csv
	print_data(ids, names, prices, amounts);
}

