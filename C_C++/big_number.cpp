#include <cstdlib>

#include "big_number.h"

BigNum::BigNum(const string s){
	string str = s;
	if(str.empty())
		throw "string empty";
	if(str[0] == '-'){
		if(str.size() < 2)
			throw "string not correct";
		else
			negatif = true;
			str.erase(0,1);
	}
	else
		negatif = false;

	for (int i = str.size() ; i > 0 ; i -= DIGIT){
		if(i - DIGIT <= 0)
			listeNumbers.push_back(strtoll(str.substr(0, i).c_str(), NULL, 10));
		else
			listeNumbers.push_back(strtoll(str.substr(i - DIGIT, DIGIT).c_str(), NULL, 10));
	}
}

BigNum::BigNum(const BigNum& other){
	listeNumbers = other.listeNumbers;
	negatif = other.negatif;
}

BigNum::BigNum(long long int i){
	if(i < 0)
		negatif = true;
	else
		negatif = false;

	listeNumbers.push_back(i);
}

BigNum& BigNum::operator = (const BigNum& other){
	listeNumbers = other.listeNumbers;
	negatif = other.negatif;
	return *this;
}

BigNum& BigNum::operator = (long long int i){
	listeNumbers.clear();
	if(i < 0)
		negatif = true;
	else
		negatif = false;

	listeNumbers.push_back(i);
}

BigNum BigNum::operator / (BigNum& other){
	if(listeNumbers.size() < other.listeNumbers.size()){
		return BigNum("0");
	}
	else if(listeNumbers.size() == other.listeNumbers.size()){
		vector<long long int>::reverse_iterator it1 = listeNumbers.rbegin();
		vector<long long int>::reverse_iterator it2 = other.listeNumbers.rbegin();
		bool ok = false;
		while(!ok && it1 < listeNumbers.rend()){
			if(*it1 < *it2){
				return BigNum("0");
			}
			else if(*it1 < *it2)
				ok = true;
			it1++;
			it2++;
		}
	}

	BigNum temp = other;
	BigNum diff = *this - temp;
	unsigned long long int i = 0;
	while((diff.listeNumbers.back() & 0x8000000000000000) == 0){
		temp = temp + other;
		diff = *this - temp;
		i++;
	}
	BigNum res(i);
	if((negatif && !other.negatif) || (!negatif && other.negatif))
		res.negatif = true;
	else
		res.negatif = false;
	return res;
}

BigNum BigNum::operator * (BigNum& other){
	BigNum res;

	if((negatif && !other.negatif) || (!negatif && other.negatif))
		res.negatif = true;
	else
		res.negatif = false;

	vector<long long int>* pMin;
	vector<long long int>* pMax;

	if(listeNumbers.size() > other.listeNumbers.size()){
		pMin = &(other.listeNumbers);
		pMax = &listeNumbers;
	}
	else{
		pMin = &listeNumbers;
		pMax = &(other.listeNumbers);
	}

	vector<long long int>::iterator itMin = pMin->begin();
	vector<long long int>::iterator itMax = pMax->begin();
	long long int temp = 0;
	long long int temp2 = 0;
	long long int tempAvRetenue;
	long long int tempApRetenue;
	long long int tempAvReste;
	long long int tempApReste;
	unsigned long long int i = 0;
	unsigned long long int j = 0;
	bool exist = false;

	while(itMin < pMin->end()){
		tempAvRetenue = 0;
		tempAvReste = 0;
		vector<short int> listeDigits;

		for(unsigned long long int m = 1 ; m < 100000000000000000 ; m *= 10 )
			listeDigits.push_back((*itMin % (m * 10)) / m);

		while(itMax < pMax->end()){
			tempApReste = 0;
			tempApRetenue = 0;
			if(res.listeNumbers.size() > (i + j)){
				temp = res.listeNumbers.at(i + j);
				exist = true;
			}
			else
				exist = false;

			temp = temp + tempAvRetenue + tempAvReste;
			if((tempApRetenue = temp / 100000000000000000) != 0)
				temp = temp % 100000000000000000;

			unsigned long long int k = 1;
			for(unsigned long long int m = 0 ; m < DIGIT ; m++){
				if((tempApReste += ((*itMax * listeDigits.at(m)) / (100000000000000000 / k))) != 0)
					temp2 += (((*itMax * listeDigits.at(m)) % (100000000000000000 / k)) * k);
				else
					temp2 += (*itMax * listeDigits.at(m) * k);

				if((tempApReste += (temp2 / 100000000000000000)) != 0)
					temp2 = temp2 % 100000000000000000;

				k *= 10;
			}

			temp += temp2;
			if((tempApRetenue += temp / 100000000000000000) != 0)
				temp = temp % 100000000000000000;

			if(exist)
				res.listeNumbers.at(i + j) = temp;
			else
				res.listeNumbers.push_back(temp);

			tempAvRetenue = tempApRetenue;
			tempAvReste = tempApReste;
			temp = 0;
			temp2 = 0;
			j++;
			itMax++;
		}
		if(tempAvReste != 0 || tempAvRetenue != 0){
			if(res.listeNumbers.size() > (i + j)){
				temp = res.listeNumbers.at(i + j);
				exist = true;
			}
			else
				exist = false;

			temp = temp + tempAvRetenue + tempAvReste;
			if((tempApRetenue = temp / 100000000000000000) != 0)
				temp = temp % 100000000000000000;

			if(exist)
				res.listeNumbers.at(i + j) = temp;
			else
				res.listeNumbers.push_back(temp);

			tempAvRetenue = tempApRetenue;
			j++;

			while(tempAvRetenue != 0){
				if(res.listeNumbers.size() > (i + j)){
					temp = res.listeNumbers.at(i + j);
					exist = true;
				}
				else
					exist = false;

				temp = temp + tempAvRetenue;
				if((tempApRetenue = temp / 100000000000000000) != 0)
					temp = temp % 100000000000000000;

				if(exist)
					res.listeNumbers.at(i + j) = temp;
				else
					res.listeNumbers.push_back(temp);

				tempAvRetenue = tempApRetenue;
				j++;
			}
		}
		j = 0;
		itMax = pMax->begin();
		itMin++;
		i++;
	}
	return res;
}

BigNum BigNum::operator - (BigNum& other){
	other.negatif = !other.negatif;
	return (*this + other);
}

BigNum BigNum::operator + (BigNum& other){
	BigNum res;
	res.negatif = false;

	vector<long long int>* pMin = NULL;
	vector<long long int>* pMax = NULL;

	if(listeNumbers.size() > other.listeNumbers.size()){
		pMin = &(other.listeNumbers);
		pMax = &listeNumbers;
		if(negatif)
			res.negatif = true;
	}
	else if(listeNumbers.size() < other.listeNumbers.size()){
		pMin = &listeNumbers;
		pMax = &(other.listeNumbers);
		if(other.negatif)
			res.negatif = true;
	}
	else{
		vector<long long int>::reverse_iterator it1 = listeNumbers.rbegin();
		vector<long long int>::reverse_iterator it2 = other.listeNumbers.rbegin();
		while(it1 < listeNumbers.rend() && pMin == NULL){
			if(*it1 > *it2){
				pMin = &(other.listeNumbers);
				pMax = &listeNumbers;
				if(negatif)
					res.negatif = true;
			}
			else if(*it1 < *it2){
				pMin = &listeNumbers;
				pMax = &(other.listeNumbers);
				if(other.negatif)
					res.negatif = true;
			}
			it1++;
			it2++;
		}
		if(pMin == NULL){
			pMin = &listeNumbers;
			pMax = &(other.listeNumbers);
		}
	}

	vector<long long int>::iterator itMin = pMin->begin();
	vector<long long int>::iterator itMax = pMax->begin();

	short int retenue = 0;
	long long int temp;
		
	if((negatif && !other.negatif) || (!negatif && other.negatif)){

		while(itMin < pMin->end()){
			temp = *itMax - *itMin - retenue;
			if(temp < 0)
			{
				temp += 100000000000000000;
				retenue = 1;
			}

			res.listeNumbers.push_back(temp);
			
			itMin++;
			itMax++;
		}
		while(itMax < pMax->end())
		{
			if(retenue){
				temp = *itMax - retenue;
				if(temp < 0)
					temp += 100000000000000000;
				else
					retenue = 0;
				res.listeNumbers.push_back(temp);
			}
			else
				res.listeNumbers.push_back(*itMax);
			itMax++;
		}

		while(res.listeNumbers.back() == 0 && res.listeNumbers.size() > 1)
			res.listeNumbers.pop_back();
	}
	else{
		if(negatif && other.negatif)
			res.negatif = true;

		while(itMin < pMin->end()){
			temp = (*itMin) + (*itMax) + retenue;
			if((retenue = (temp / 100000000000000000)) != 0)
			{
				temp = temp % 100000000000000000;
			}
			res.listeNumbers.push_back(temp);
			itMin++;
			itMax++;
		}

		while(itMax < pMax->end()){
			if(retenue != 0){
				if(*itMax != 99999999999999999){
					res.listeNumbers.push_back(retenue + *itMax);
					itMax ++;
					retenue = 0;
				}
				else{
					res.listeNumbers.push_back(0);
					itMax++;
				}
			}
			else{
				while(itMax < pMax->end()){
					res.listeNumbers.push_back(*itMax);
					itMax ++;
				}
				return res;
			}
		}
		if(retenue != 0)
			res.listeNumbers.push_back(retenue);
		return res;
	}
}

int main(){
	BigNum j("-1000000000000000000000000");
	BigNum i("20000000000000000000000000000000000000000000000");
	j = j + i;
	cout << j <<endl;
	//15 minutes multiplication 745000 numbers (500000 * 280000) ; 19 minutes multiplication 745000 numbers (350000 * 390000)
	//4.2 seconds addition 548000 numbers
	//2.0 seconds soustraction 548000numbers
}