#include "create_book.h"
using namespace std;

// ##### INIT CONNECTION:
Connection connection;
MYSQL* conn = connection.make_connection();

vector<string> fetchone(string title){
	vector<string> row_data;
	const char* query = "SELECT * FROM books WHERE title_book = \'%s\';";
	int size_of_query = snprintf(nullptr, 0, query, title.c_str());
	char consult[size_of_query]; 
	snprintf(consult, sizeof(consult), query, title.c_str());
	
	if(!mysql_query(conn, consult)){
		connection.result = mysql_store_result(conn);
		connection.row = mysql_fetch_row(connection.result);
		
		if(connection.row){
			for(unsigned int i = 0; i<mysql_num_fields(connection.result); i++){
            	row_data.push_back(connection.row[i] ? connection.row[i] : "NULL"); 
        	}
		}
	}
	else{
		cout<<"\nError. "<<mysql_error(conn);
	}
	return row_data;
}
// #########################################################################
void print_header(){
	cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl; //SEPERATOR

	cout<<"\t"<<
	setfill(' ')<<left<<setw(15)<<"# ID"<<
	setfill(' ')<<left<<setw(30)<<"Title"<<
	setfill(' ')<<left<<setw(35)<<"Author"<<
	setfill(' ')<<left<<setw(15)<<"Year"<<
	setfill(' ')<<left<<setw(5)<<"Quantity"<<endl;

	cout<<setfill('_')<<right<<setw(120)<<"\t"<<endl;  //SEPERATOR
}
// #########################################################################
void show_books(){
	if(!mysql_query(conn, "SELECT * FROM books;")){
		print_header();
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
		cout<<"\nThe books could not be showed."<<endl;
	}
	mysql_free_result(connection.result);
}
// #########################################################################
void insert_book(Book book){
	vector<string> data = fetchone(book.title);
	if(data.size()!=0){
		cout<<"\nThe book is already registered, go to the menu option to update the number of available books.\n";
		return;
	} 

	const char* query = "INSERT INTO books (id_book, title_book, author_book, year_book, quantity_book) VALUES (\'%s\', \'%s\', \'%s\', %d, %d);";
	
	// ##### GETTING THE QUERY SIZE ALONG WITH THE PARAMETERS
	int size_of_query = snprintf(nullptr, 0, query, book.id.c_str(), book.title.c_str(), book.author.c_str(), book.year, book.quantity);
	// ###### BUFFER SIZE WITHOUT NULL CHARACTERS '\0'
	char consult[size_of_query]; 
	// #### FORMATTING THE QUERY AND SAVING IT IN CONSULT
	snprintf(consult, sizeof(consult), query, book.id.c_str(), book.title.c_str(), book.author.c_str(), book.year, book.quantity);

	if(!mysql_query(conn, consult)){
		cout<<"\nBook inserted!"<<endl;
	}else{
		cout<<"\nError. "<<mysql_error(conn);
	}
}
// #########################################################################
void update_book(string id, int quantity){
	const char* query = "UPDATE books SET quantity_book = quantity_book + %d WHERE id_book = \'%s\';";
	int size_of_query = snprintf(nullptr, 0, query, quantity, id.c_str());
	char consult[size_of_query]; 
	snprintf(consult, sizeof(consult), query, quantity, id.c_str());

	if(!mysql_query(conn, consult)){
		cout<<"\nQuantity book updated!"<<endl;
	}else{
		cout<<"\nError. "<<mysql_error(conn);
	}
}

void delete_book(string id){
	const char* query = "DELETE FROM books WHERE id_book = \'%s\';";
	int size_of_query = snprintf(nullptr, 0, query, id.c_str());
	char consult[size_of_query]; 
	snprintf(consult, sizeof(consult), query, id.c_str());
 
	if(!mysql_query(conn, consult)){
		cout<<"\nBook deleted!"<<endl;
	}else{
		cout<<"\nError. "<<mysql_error(conn);
	}
}

void search_book(string title){
	vector<string> book_get = fetchone(title);
	print_header();
	for(int k = 0 ;  k<book_get.size(); k++){
		cout << "\t" << setfill(' ') << left 
       	<< setw(k == 0 ? 5 : (k == 1 ? 30 : (k == 2 ? 30 : (k == 3 ? 10 : 15)))) 
        <<book_get[k];
	}
	cout<<endl;
}