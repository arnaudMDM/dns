#ifndef _BIG_NUM_
#define _BIG_NUM_
#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <cstdio>

#define DIGIT 17

using namespace std;

class BigNum{
public:
	BigNum(){};
	BigNum(const string s);
	~BigNum(){};
	BigNum(const BigNum& other);
	BigNum(long long int i);
	vector<long long int>& getListeNumbers(){
		return listeNumbers;
	}
	BigNum& operator = (const BigNum& other);
	BigNum& operator = (long long int i);
	BigNum operator + (BigNum& other);
	BigNum operator - (BigNum& other);
	BigNum operator * (BigNum& other);
	BigNum operator / (BigNum& other);
protected:
	vector<long long int> listeNumbers;
};

ostream& operator << (ostream& os, BigNum& bigNum){
	vector<long long int> liste = bigNum.getListeNumbers();
	char buffer[DIGIT + 2];
	vector<long long int>::reverse_iterator it = liste.rbegin();
	while(it < liste.rend()){
		if(it != liste.rbegin())
			sprintf(buffer,"%.17lld",*it);
		else{
			if((*it & 0x8000000000000000) != 0){
				buffer[0] = '-';
				sprintf(buffer+1,"%lld",(*it & 0x7fffffffffffffff));
			}
			else
				sprintf(buffer,"%lld",(*it & 0x7fffffffffffffff));
		}
		os << buffer;
		it++;
	}
	return os;
}

#endif