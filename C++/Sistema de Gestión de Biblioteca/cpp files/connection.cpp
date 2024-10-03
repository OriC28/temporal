#include<iostream>
#include<mysql.h>
#include<mysqld_error.h>
using namespace std;

class Connection{
private:
	char HOST[20] = "localhost";
	char USER[20] = "root";
	char PASSWORD[20] = "Ori31525588$$.";
	char DATABASE[20] = "biblioteca_db";
	int PORT = 3306;
	MYSQL* conn;

public:
	MYSQL* make_connection(){	
		conn = mysql_init(0);
		MYSQL* connected;
		connected = (mysql_real_connect(conn, HOST, USER, PASSWORD, DATABASE, PORT, NULL, 0))==nullptr ? nullptr:conn;
		return connected;
	}
};

