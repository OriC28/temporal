#include<iostream>
#include<algorithm>
#include<random>
#include<vector>
using namespace std;

int factorial(int n){
  return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

vector<string> permutation(vector<string> words){
	vector<string> permu_words;
	bool same_size = true;
	int size = words[0].length(), temp_size; // 
	
	// CHECK IF ALL WORDS HAVE THE SAME SIZE
	for(int i=1; i<words.size(); i++){
		if(words[i].length() == size){
			temp_size = size;
			size = words[i].length();
		}else{
			same_size = false;
			break;
		}
	}

	// IF ALL WORDS HAVE THE SAME SIZE SO IT'LL GENERATE ALL PERMUTATION
	if(same_size){
		int l = 0;
		int r = factorial(words.size()); // IT'S THE QUANTITY OF PERMUTATIONS NECESSARY
		random_device rd;
		mt19937 g(rd());
		string word, temp;
		while(l<r){
			shuffle(words.begin(), words.end(), g); // MIX THE WORDS'S VECTOR
			for(auto& x : words){
				word+=x; // GENERATING COMBINATION
			}
			if (word!=temp && temp!=""){
				// IN CASE TO REPEATS MIX NEWLY THE WORDS'S VECTOR
				if(find(permu_words.begin(), permu_words.end(), word) != permu_words.end()){
					shuffle(words.begin(), words.end(), g);
				}
				// IF NOT, ADD THE NEW PERMUTATION IN THE VECTOR
				else{
					permu_words.push_back(word);
					l++;
				}
			}
			// UPDATE THE VARIABLES
			temp = word;
			word = "";
		}
	}
	return permu_words;
}


vector<int> findSubstring(string s, vector<string>& words){
	vector<string> permu_words = permutation(words);
	vector<int> positions;
	// FINDING THE POSITIONS OF EACH WORD IF THIS IS FOUND INTO MAIN WORD
	for(string i : permu_words){
		if(s.find(i) != std::string::npos){
			positions.push_back(s.find(i));
		} 
	}

	return positions;
}

int main(int argc, char const *argv[]){
	vector<string> words = {"bar","foo"};
	vector<int> positions_words = findSubstring("barfoothefoobarman", words);
	// SHOWING POSITIONS
	for(auto& i : positions_words){
		cout<<i<<" ";
	}
	return 0;
}

