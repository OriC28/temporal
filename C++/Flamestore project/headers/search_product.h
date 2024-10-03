#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
using namespace std;

void search_product();

void search_product(){
	string id_to_search;
	vector<string> ids, names, prices, amounts;
	
	cout<<"\nEnter the ID of the product to search: ";
	cin>>id_to_search;

	if (id_to_search.length()!=8){
		cout<<"\nInvalid ID, please verify the ID and try again.\n\n";
	}
	else{

		// ########## GET DATA INTO CSV FILE
		get_dataCSV(ids, names, prices, amounts); // get_dataCSV is defined into "get_data.h" included in main.cpp

		//###### HEADER 
		get_header();

		for(int i=0; i<ids.size(); i++){
			if(id_to_search == ids[i]){
				cout<<"\t"<<
					setfill(' ')<<left<<setw(15)<<ids[i]<<
					setfill(' ')<<left<<setw(50)<<names[i]<<
					setfill(' ')<<left<<setw(10)<<prices[i]<<
					setfill(' ')<<left<<setw(20)<<amounts[i]<<endl;

					cout<<setfill('-')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR
			}
		}
	}
}