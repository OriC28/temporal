#include<iostream>
#include<iomanip>
#include<mysql.h>
#include<mysqld_error.h>
#include "connection.h"
using namespace std;

Connection connection;
MYSQL* conn = connection.make_connection();

void show_data();

int main(){
	cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl; //SEPERATOR

	cout<<"\t"<<
	setfill(' ')<<left<<setw(15)<<"# ID"<<
	setfill(' ')<<left<<setw(30)<<"Title"<<
	setfill(' ')<<left<<setw(35)<<"Author"<<
	setfill(' ')<<left<<setw(15)<<"Year"<<
	setfill(' ')<<left<<setw(5)<<"Quantity"<<endl;

	cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl;  //SEPERATOR

	show_data();
	return 0;
}


void show_data(){
	if(!mysql_query(conn, "SELECT * FROM books;")){

		connection.result = mysql_store_result(conn);
		// ##### NUMBER OF COLUMNS IN THE TABLE
   		int columns = mysql_num_fields(connection.result);
   		// ##### WHILE WE GO THROUGH THE ROWS WITHIN THE TABLE 
		while(connection.row = mysql_fetch_row(connection.result)){
			for(int k = 0 ;  k<columns ; k++){
				// ##### IF SOME ITEM IS EMPTY WRITE NULL ELSE JUST WRITE ITEM ROW 
				cout << "\t" << setfill(' ') << left 
                     << setw(k == 0 ? 5 : (k == 1 ? 30 : (k == 2 ? 30 : (k == 3 ? 10 : 15)))) 
                     << ((connection.row[k] == NULL) ? "NULL" : connection.row[k]);
			}
			cout<<endl;
		}
	}else{
		cout<<"The books could not be showed."<<endl;
	}
	mysql_close(conn);
}