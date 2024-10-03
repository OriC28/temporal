#include<iostream>
#include<ctime>
#include<random>
#include<vector>
#include<iomanip>
#include<mysql.h>
#include<mysqld_error.h>
#include "headers/connection.h"
#include "headers/books_queries.h"
#include "headers/users_queries.h"
using namespace std;

string  generate_id();
void menu();

int main(){
	menu();
	return 0;
}

void menu(){
	int option=0;
	while(option==0 || option>9 || option<0){
		system("CLS");
		cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl;
		cout<<"\t\t\t1. Add new book\n";
		cout<<"\t\t\t2. Update available book\n";
		cout<<"\t\t\t3. Delete book\n";
		cout<<"\t\t\t4. Search book\n";
		cout<<"\t\t\t5. Show books\n";
		cout<<"\t\t\t6. Register user\n";
		cout<<"\t\t\t7. Register loan\n";
		cout<<"\t\t\t8. Register return\n";
		cout<<"\t\t\t9. Most borrowed books (report)\n";
		cout<<"\t\t\t0. Exit\n";
		cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl;
		cout<<"\n"<<setfill('_')<<right<<setw(120)<<"\t"<<endl;
		cout<<"\t\t\tOption: "; cin>>option;

		switch(option){
			case 1:{
				system("CLS");
				string title, author;
				int year, quantity;
				cin.ignore();
				cout<<"Enter title: ";
				getline(cin, title);
				cout<<"Enter author: ";
				getline(cin, author);
				cout<<"Enter year: ";
				cin>>year;
				cout<<"Enter quantity: ";
				cin>>quantity;
				if(title!="" && author!="" && year>0 && quantity>0){
					Book book(title, author, year, quantity);
					insert_book(book);
				}else{
					cout<<"\nEnter valid date."<<endl;
				}
				mysql_close(conn);
				break;
			}
			case 2:{
				system("CLS");
				string id;
				int quantity;
				cin.ignore();
				show_books();
				cout<<"\nEnter ID of book to updated: ";
				cin>>id;
				cout<<"Enter the quantity to add: ";
				cin>>quantity;
				if (id!="" && quantity>0){
					update_book(id, quantity);
				}else{
					cout<<"\nError. Enter valid date."<<endl;
				}
				mysql_close(conn);
				break;
			}
			case 3:{
				system("CLS");
				string id_book;
				cin.ignore();
				show_books();
				cout<<"\nEnter the book's id to delete: ";
				cin>>id_book;
				delete_book(id_book);
				break;
			}
			case 4:{
				system("CLS");
				string title;
				cin.ignore();
				cout<<"\nEnter the book's title to search: ";
				getline(cin, title);
				search_book(title);
				break;
			}
			case 5:
				system("CLS");
				show_books();
				mysql_close(conn);
				system("PAUSE");
				system("CLS");
				break;
			case 6:{
				system("CLS");
				string cedula, name, address;
				cout<<"Enter C.I: ";
				cin>>cedula;
				cin.ignore(256, '\n');
				cout<<"Enter name and last name: ";
				getline(cin, name);
				cout<<"Enter address: ";
				getline(cin, address);
				User user(cedula, name, address);
				register_user(user);
				mysql_close(conn);
				break;
			}
			case 0: system("PAUSE"); exit(0);
			default: system("PAUSE"); cout<<"\nIncorrect option, try again.\n"; 
		}
	}
}



