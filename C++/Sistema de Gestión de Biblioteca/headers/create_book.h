using namespace std;

class Book{
public:
	string id = generate_id();
	string title;
	string author;
	int year;
	int quantity;
	Book(string title, string author, int year, int quantity){
		this->title = title;
		this->author = author;
		this->year = year;
		this->quantity = quantity;
	}
	string generate_id(){
		srand((unsigned)time(NULL));
		string id;
		vector<char> letters;
		vector<char> alphabet;
		vector<char> digits = {'0','1','2','3','4','5','6','7','8','9'};
		for(char i='A'; i<='Z'; i++){alphabet.push_back(i);}

		letters.insert(letters.begin(), alphabet.begin(), alphabet.end());
		letters.insert(letters.end(), digits.begin(), digits.end());
			

		for(int i=0; i<10; i++){
			int character = rand() % (36-0) + 0;
			id+=letters[character];
		}
		return id;
	}
};
