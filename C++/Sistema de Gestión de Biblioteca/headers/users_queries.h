#include "users.h"
using namespace std;

void register_user(User user){
	const char* query = "INSERT INTO users(ci_user, name_user, address_user) VALUES (\'%s\',\'%s\',\'%s\');";
	int size_of_query = snprintf(nullptr, 0, query, user.cedula.c_str(), user.name.c_str(), user.address.c_str());
	char consult[size_of_query];
	snprintf(consult, sizeof(consult), query, user.cedula.c_str(), user.name.c_str(), user.address.c_str());
	if(!mysql_query(conn, consult)){
		cout<<"User registered."<<endl;
	}else{
		cout<<"Error. "<<mysql_error(conn);
	}
}

