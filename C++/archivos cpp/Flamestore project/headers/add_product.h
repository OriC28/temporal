#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<fstream> //*** TO USE FSTREAM, OFSTREAM AND IFSTREAM OBJECT
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include <ctime> //*** TO USE FUNCTION TIME
#include<random> ///*** TO USE SRAND AND RAND FUNCTIONS
using namespace std;

bool create_csv();
void get_product();
void add_product(string, string, int, float);

class Product{
public:
	string id = generate_id();
	string name;
	int amount;
	float price;

	//************** Constructor *****************
	Product(string name, int amount, float price){
		this->name = name;
		this->amount = amount;
		this->price = price;
	}

	string generate_id(){
		srand(std::time(nullptr));
		string id;
		vector<char> letters;
		vector<char> alphabet;
		vector<char> digits = {'0','1','2','3','4','5','6','7','8','9'};
		for(char i='A'; i<='Z'; i++){alphabet.push_back(i);}

		letters.insert(letters.begin(), alphabet.begin(), alphabet.end());
		letters.insert(letters.end(), digits.begin(), digits.end());
		

		for(int i=0; i<8; i++){
			int character = rand() % (36-0) + 0;
			id+=letters[character];
		}
		return id;
	}
};

void get_product(){
	system("cls");
	string name;
	int amount;
	float price;
	cin.ignore(256, '\n');
	cout<<"Enter name product: ";
	getline(cin, name);
	cout<<"Enter amount product: ";
	cin>>amount;
	cout<<"Enter price product: ";
	cin>>price;
	if(name!="" && amount>0 && price>0){
		Product product(name, amount, price);
		add_product(product.id, name, amount, price);
	}
}

void add_product(string id, string name, int amount, float price){
	string filename = "./csv/products.csv";
	ifstream file(filename);
	if(file.good()){
		file.close();
		ofstream outfile(filename, ios::app);
		if(outfile.is_open()){
  			outfile<<id<<";"<<name<<";"<<price<<";"<<amount<<"\n";
  			outfile.close();
		}
		else{cerr<<"Error. Can't add the product.";}
	}	

	else{
		ofstream outfile(filename);
		if(outfile.is_open()){
			outfile<<"#"<<";"<<"Name"<<";"<<"Price"<<";"<<"Amount"<<"\n";
			outfile<<id<<";"<<name<<";"<<price<<";"<<amount<<"\n";
  			outfile.close();
		}
		else{
			cerr<<"Error. File can't open.";
		}
	}
}
