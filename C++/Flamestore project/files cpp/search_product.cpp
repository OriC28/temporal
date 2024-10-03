#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<fstream> //*** TO USE FSTREAM, OFSTREAM AND IFSTREAM OBJECT
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<sstream> //*** TO USE CLASS STRINGSTREAM
#include<iomanip> //*** TO USE SETW, SETFILL FUNCTIONS
using namespace std;

void search_product();

int main(){
	search_product();

	return 0;
}

void search_product(){
	system("cls");
	string line, id_to_search, id_get, name, price, amount;
	vector<string> ids, names, prices, amounts;
	char delimiter = ';';
	ifstream file("products.csv");

	cout<<"Enter the ID of the product to search: ";
	cin>>id_to_search;

	if(!file.is_open()){
		cout<<"\nError. File not found or not readable.";
		exit(EXIT_FAILURE);
	}

	if (id_to_search.length()==8){
		getline(file, line);
		while(getline(file, line)){
			stringstream stream(line);
				getline(stream, id_get, delimiter);
			ids.push_back(id_get);
				getline(stream, name, delimiter);
			names.push_back(name);
				getline(stream, price, delimiter);
			prices.push_back(price);
				getline(stream, amount, delimiter);
			amounts.push_back(amount);		
		}

		//###### HEADER 

		cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl; //SEPERATOR

		cout<<"\t"<<
		setfill(' ')<<left<<setw(15)<<"#"<<
		setfill(' ')<<left<<setw(50)<<"Name"<<
		setfill(' ')<<left<<setw(10)<<"Price"<<
		setfill(' ')<<left<<setw(20)<<"Amount"<<endl;

		cout<<setfill('_')<<right<<setw(115)<<"\t"<<endl;  //SEPERATOR

		for(int i=0; i<ids.size(); i++){
			if(id_to_search == ids[i]){
				cout<<"\t"<<
				setfill(' ')<<left<<setw(15)<<ids[i]<<
				setfill(' ')<<left<<setw(50)<<names[i]<<
				setfill(' ')<<left<<setw(10)<<prices[i]<<
				setfill(' ')<<left<<setw(20)<<amounts[i]<<endl;

				cout<<setfill('-')<<right<<setw(115)<<"\t"<<endl; //SEPERATs
			}
		
		}
	}else{
		cout<<"\nProduct not found, check ID and try again.";
	}

}