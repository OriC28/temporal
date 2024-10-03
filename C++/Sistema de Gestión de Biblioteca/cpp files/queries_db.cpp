#include<iostream>
#include<mysql.h>
#include<mysqld_error.h>
#include<string>
#include "connection.h"
using namespace std;

// ##### INIT CONNECTION:
Connection connection;
MYSQL* conn = connection.make_connection();


// ##### DABASE FUNCTIONS:

void show_data();
void insert_data(string, string, string, int, int);
int main(){
	if(conn){
		cout<<"Success!"<<endl;
	}
	//show_data();
	insert_data();
	return 0;
}

void show_data(){
	if(!mysql_query(conn, "SELECT * FROM books")){

		connection.result = mysql_store_result(conn);
   		int columns = mysql_num_fields(connection.result);

		while(connection.row = mysql_fetch_row(connection.result)){
			for(int k = 0 ;  k<columns ; k++){
				cout<<((connection.row[k]==NULL) ? "NULL" : connection.row[k])<<endl;
			}
		}	
	}
}

void insert_data(string id, string title, string author, int year, int quantity){

	const char* query = "INSERT INTO books (id_book, title_book, author_book, year_book, quantity_book) VALUES (\'%s\', \'%s\', \'%s\', %d, %d);";
	int size_of_query = snprintf(nullptr, 0, query, first_name.c_str(), last_name.c_str(), state.c_str(), city.c_str(), email.c_str());
	char consult[size_of_query];
	snprintf(consult, sizeof(consult), query, id.c_str(), title.c_str(), author.c_str(), year, quantity);

	if(!mysql_query(conn, consult)){
		cout<<"Data inserted!"<<endl;
	}else{
		cout<<"Error. "<<mysql_error(conn);
	}
}