#include <iostream> 
using namespace std; 
class Hospital{ 
 public: 
 void bill(long int mb,int days){ 
 cout<<mb*days<<endl; 
 } 
 void bill(int rr,int days){ 
 cout<<rr*days; 
 } 
}; 
int main() 
{ 
 Hospital ob; 
 long int mbill;
 int d, rent; 
 cout<<"Enter the medical bill expense: ";
 cin>>mbill;
 cout<<"Enter the number of days: ";
 cin>>d;
 ob.bill(mbill,d); 
 cout<<"Enter the room rent: ";
 cin>>rent;
 cout<<"Enter the number of days: ";
 cin>>d; 
 ob.bill(rent,d); 
 return 0; 
} 
