#include <iostream>
using namespace std;
class Account{
    int acc_Id;
    char name[50];
    float bal;
    
    public:
    Account()
    { cout<<"ZERO BALANCE"<<endl;}
    Account(float bal)
    {
        if (bal>0)
        {cout<<"Account Balance is POSITIVE"<<endl;}
        else if (bal<0)
        {cout<<"Account balance is NEGATIVE"<<endl;}
        else{cout<<"ZERO BALANCE"<<endl;}
    }
    
};
int main()
{float bal;
cout<<"Enter your current balance: ";
cin>>bal;
Account();
Account r(bal);
return 0;}
