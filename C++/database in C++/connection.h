#include <iostream>
#include <mysql.h>
#include <mysqld_error.h>
#include "students.h"
using namespace std;

class Connection{
	public:
		const char* HOST;
		const char* USER;
		const char* PASSWORD;
		const char* DATABASE;
		int PORT;
		MYSQL * conn;
		char *query;
	
		Connection(const char* HOST, const char* USER, const char* PASSWORD, const char* DATABASE, int PORT){
			this->HOST = HOST;
			this->USER = USER;
			this->PASSWORD= PASSWORD;
			this->DATABASE= DATABASE;
			this->PORT = PORT;
			this->conn = make_connection();
		}
		
		MYSQL * make_connection(){
			MYSQL * connected;
			MYSQL* connection;
			connection = mysql_init(0);
			connection = mysql_real_connect(connection, HOST, USER, PASSWORD, DATABASE, PORT, NULL, 0);
			connected = (connection) ? connection: nullptr;
			return connected;
		}
		bool execute_query(char *query){
			const char* c = query;
			bool q_status = mysql_query(conn, c);
			return q_status;
		}
		MYSQL_RES* get_result(){
			MYSQL_RES* result;
			result = mysql_store_result(conn);
			return result;
		}
		
		void show_data(){
			MYSQL_ROW row;
			MYSQL_RES* result;
			char *query = "SELECT * FROM students";
			bool q_status = execute_query(query);
			if(!q_status){
				result = get_result();
				int rows = mysql_num_rows(result);
   				int columns = mysql_num_fields(result);

				while(row = mysql_fetch_row(result)){
					for(int k = 0 ;  k<columns ; k++){
						cout<<((row[k]==NULL) ? "NULL" : row[k])<<endl;
					}
				}	
			}	
			else{
				cout<<"Error, could not be connection."<<endl;
			}
			mysql_close(conn);
		}
		void insert_data(Student student){
			char operation[] = "INSERT INTO students (first_name, last_name, state, city, emailAddress) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')";
			query = new char[strlen(operation) + strlen(student.first_name) + strlen(student.last_name) + strlen(student.state) + strlen(student.city) + strlen(student.email) + 1];
			sprintf(query, operation, student.first_name, student.last_name, student.state, student.city, student.email);
			bool q_status = execute_query(query);
			if(!q_status){
				cout<<"Data inserted successfully."<<endl;
			}else{
				cout<<"Data could not be insert. "<<mysql_error(conn)<<endl;
			}
			delete[] query;
		}
		
		void update_email(Student student){
			char operation[] = "UPDATE students SET emailAddress = '\%s\' WHERE first_name = \'%s\'";
			query = new char[strlen(operation) + strlen(student.email) + strlen(student.first_name) + 1];
			sprintf(query, operation, student.email, student.first_name);
			bool q_status = execute_query(query);
			if(!q_status){
				cout<<"Email updated successfully."<<endl;
			}else{
				cout<<"Error. Email could not be updated. "<<mysql_error(conn)<<endl;
			}
			delete[] query;
		}
		
		void delete_data(Student student){
			char operation[] = "DELETE FROM students WHERE first_name = \'%s\'";
			query = new char[strlen(operation) + strlen(student.first_name) + 1];
			sprintf(query, operation, student.first_name);
			bool q_status = execute_query(query);
			if(!q_status){
				cout<<"Email updated successfully."<<endl;
			}else{
				cout<<"Error. Email could not be updated. "<<mysql_error(conn)<<endl;
			}
			delete[] query;
		}
};



