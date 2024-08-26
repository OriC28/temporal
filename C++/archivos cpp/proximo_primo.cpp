#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> get_dividers(int);
bool is_prime(int);
int next_prime_of(int);

int main(){
	int num = 43;
	cout<<"The next prime number of "<<num<<" is: "<<next_prime_of(num);
	return 0;
}

vector<int> get_dividers(int num){
	vector <int> dividers;
	for(int i=2; i<=num+10; i++){
		dividers.push_back(i);
	}
	return dividers;
}

bool is_prime(int num){
	int count = 0;
	vector <int> divs;
	divs = get_dividers(num);
	for(int i=0; i<divs.size(); i++){
		if(num % divs[i] == 0){count++;}
	}
	count = (count>1) ? false : true;
	return count;
}

int next_prime_of(int num){
	int result;
	vector <int> primes;
	vector <int> divs;
	divs = get_dividers(num);
	copy_if(divs.begin(), divs.end(), back_inserter(primes), [](int i){return is_prime(i);});

    for (int &i: primes){
    	if(i>num){result = i; break;}
    }
    return result;
}


