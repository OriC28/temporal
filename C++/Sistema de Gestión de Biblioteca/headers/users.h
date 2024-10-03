using namespace std;

class User{
public:
	string cedula;
	string name;
	string address;

	User(string cedula, string name, string address){
		this->cedula = cedula;
		this->name = name;
		this->address = address;
	}
}; 