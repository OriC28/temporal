#include<iostream> //****TO USE CIN, COUT, GETLINE, CIN.IGNORE
#include<vector> //*** TO USE VECTOR CLASS AND HIS METHODS
#include<windows.h> //*** TO USE ShellExecute FUNCTION
#include<ctime>
#include<sstream>
using namespace std;

void create_web();
string date_now();
void open_website();

string date_now(){
	auto t = time(nullptr);
	auto tm = *std::localtime(&t);

	ostringstream oss;
	oss<<put_time(&tm, "%d-%m-%Y");
	auto date = oss.str();
	return date;
}

void create_web(){
	vector<string> ids, names, prices, amounts;
	string date = date_now();
	ofstream web("./index.html");
	web<<"<html>"<<endl;
		web<<"<head>"<<endl;
			web<<"<title>Listado de productos</title>"<<endl;
		    web<<"<link rel=\"icon\" href=\"img/imagen.ico\">"<<endl;
            web<<"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"<<endl;
			web<<"<link rel=\"stylesheet\" href=\"css/style.css\">"<<endl;
		web<<"</head>"<<endl;
		web<<"<body>"<<endl;

			//********************** PRINCIPAL TITLE ************************
			web<<"<h1>REPORT "<<date<<"</h1>"<<endl;

			//*************************** BUTTON ******************************
			web<<"<input class=\"button\" type=\"submit\" name=\"print\" value=\"Print\">"<<endl;


			//************************ START TABLE ******************************
			web<<"<table>"<<endl;

				//*********************** HEADER *****************************
				web<<"<tr>"<<endl;
					web<<"<th># ID</th>"<<endl;
					web<<"<th>NAME</th>"<<endl;
					web<<"<th>PRICE</th>"<<endl;
					web<<"<th>AMOUNT</th>"<<endl;
				web<<"</tr>"<<endl;

				//********************** ROWS ********************************
				get_dataCSV(ids, names, prices, amounts); //get_dataCSV is defined into "get_data.h" included in main.cpp
				for(int i=0; i<ids.size(); i++){
					web<<"<tr>"<<endl;
                        web<<"<td>"<<ids[i]<<"</td>"<<endl;
                        web<<"<td>"<<names[i]<<"</td>"<<endl;
                        web<<"<td>"<<prices[i]<<"</td>"<<endl;
                        web<<"<td>"<<amounts[i]<<"</td>"<<endl;
                    web<<"</tr>"<<endl;
				}

			web<<"</table>"<<endl;
			web<<"<script rel=\"script\" src=\"js/script.js\"></script>"<<endl;
		web<<"</body>"<<endl;
	web<<"</html>"<<endl;
	web.close();
}

void open_website(){
	create_web();
	ShellExecute(GetDesktopWindow(),"open", "index.html", NULL, NULL, SW_SHOWNORMAL); 
}
