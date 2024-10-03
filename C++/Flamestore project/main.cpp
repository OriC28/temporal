#include<iostream>
#include<locale.h>
#include "headers/get_data.h"
#include "headers/login.h"
#include "headers/products.h"
#include "headers/add_product.h"
#include "headers/show_products.h"
#include "headers/search_product.h"
#include "headers/web.h"
using namespace std;

void open_system();
void log_in();
void start_options();

int main(){
	system("COLOR 70");
	setlocale(LC_ALL, "spanish");
	start_options();
	return 0;
}

void open_system(){
	int option = 0;
	bool increment_product, decrement_product;
	while(option == 0 || option>2 || option<0){
		system("cls");
		cout<<"Select an option\n\n";
		cout<<"1. Products\n";
		cout<<"2. Show products entries\n";
		cout<<"3. Dispatch of products\n";
		cout<<"4. Show products outputs\n";
		cout<<"5. Add product\n";
		cout<<"6. Show products\n";
		cout<<"7. Search product\n";
		cout<<"8. Generate web report\n";
		cout<<"0. Exit\n\n";

		cout<<"Option: "; cin>>option;

		switch(option){
			case 1: {
				while(1){
					system("cls");
					increment_product = products("input");
					if(increment_product){
						cout<<"\nQuantity has been added to the selected product, to see the changes go to \"Show product entries\" in the menu.\n";
						system("pause");
						system("cls");
						open_system();
						break;
					}
					else{
						cout<<"\nAn error has occurred, check the data entered or the existence of the products.csv file.\n";
						system("pause");
						system("cls");
						open_system();
						break;
					}
				}
				break;
			}
			case 2:{ 
				system("cls");
				system("mode con: cols=165 lines=50");
				 print_data_in_out("./csv/products_entries.csv"); system("pause");
				system("cls");
				system("mode con: cols=120 lines=30");
				open_system();
				break;
			}
			case 3:{
				while(1){
					system("cls");
					decrement_product = products("output");
					if(decrement_product){
						cout<<"\nQuantity has been updated to the selected product, to see the changes go to \"Show product outputs\" in the menu.\n";
						system("pause");
						system("cls");
						open_system();
						break;
					}
					else{
						cout<<"\nAn error has occurred, check the data entered or the existence of the products.csv file.\n";
						system("pause");
						system("cls");
						open_system();
						break;
					}
				}
				break;
			}
			case 4:
				system("cls");
				system("mode con: cols=165 lines=50");
				 print_data_in_out("./csv/products_outputs.csv"); system("pause");
				system("cls");
				system("mode con: cols=120 lines=30");
				open_system();
				break;
			case 5: get_product(); system("pause"); system("cls"); break;
			case 6: get_products_saved(); system("pause"); system("cls"); break;
			case 7: search_product(); system("pause"); system("cls"); break;
			case 8: open_website(); system("pause"); system("cls"); break;
			case 0: exit(EXIT_FAILURE); break;
			default:
				cout<<"\nPlease select a correct option.\n"<<endl;
				system("pause");
				system("cls");
				break;
		}
	}
}

void log_in(){
	bool open = false;
	while(!open){
	system("cls");
		if (get_data()) {
			open_system();
			open = true;
		}
		else {
			cout<<"\nThe user not exists, try again.\n";
			system("pause");
			system("cls");
		}
	}
}

void start_options(){
	int option=0;
	string password;
	while(option==0 || option>2 || option<0){
		system("cls");
		cout<<"1. Log in\n";
		cout<<"2. Recover password\n";
		cout<<"0. Exit\n\n";

		cout<<"Option: "; cin>>option;

		switch(option){
			case 1: log_in(); system("pause"); system("cls"); break;
			case 2:{
				while(1){
					system("cls");
					password = recover_password();
					if(password!=""){
						cout<<"\nYour password has been recovered!\nPassoword: "<<password<<endl;
						system("pause");
						system("cls");
						main();
						break;
					}else{
						cout<<"\nYour password cannot be recovered, please enter a valid username."<<endl;
						system("pause");
						system("cls"); 
					}
				}
				
				break;
			}
			case 0: exit(EXIT_FAILURE); break;
			default:
				cout<<"\nPlease select a correct option.\n";
				system("pause");
				system("cls");
				break;
		}
	}
}