#include <iostream>
#include <mysql.h>
#include <mysqld_error.h>
#include "connection.h"
using namespace std;

Connection connection("localhost", "OriC28", "Ori31525588$$.", "db_students", 3306);

void ask_data();

int main(int argc, char** argv){

	Student student;
	/*
	cout<<"Enter your first name: ";
	cin.getline(student.first_name, 45, '\n');
	
	cout<<"Enter your last name: ";
	cin.getline(student.last_name, 45, '\n');
	
	cout<<"Enter your state: ";
	cin.getline(student.state, 45, '\n');
	
	cout<<"Enter your city: ";
	cin.getline(student.city, 45, '\n');
	
	cout<<"Enter your email: ";
	cin.getline(student.email, 45, '\n');
	
	connection.insert_data(student);
	connection.delete_data(student);
	connection.update_email(student);*/
	connection.show_data();
	return 0;
}

