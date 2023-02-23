#include <iostream>
using namespace std;
class Bank{
public:
int getBalance()
{ return 0; }

};

class BankA : public Bank{
public:
void getBalance() 
{ cout<<"Money deposited in Bank A: $1000\n"; }

};

class BankB : public Bank{
public:
void getBalance() 
{ cout<<"Money deposited in Bank B: $1500\n"; }

};

class BankC : public Bank{
public:
void getBalance() 
{ cout<<"Money deposited in Bank C: $2000"; }

};

int main(){
BankA a;
a.getBalance();
BankB b;
b.getBalance();
BankC c;
c.getBalance();
return 0;
}
 

