#include <iostream>

using namespace std;
class Date {      
  public:            
    int date;
    int month;
    int year;
    int m=0;
    void datechange(){
     switch(month)
     {
         case 1: m=31;
         break;
         case 2: m=28;
         break;
         case 3: m=31;
         break;
         case 4: m=30;
         break;
         case 5: m=31;
         break;
         case 6: m=30;
         break;
         case 7: m=31;
         break;
         case 8: m=31;
         break;
         case 9: m=30;
         break;
         case 10: m=31;
         break;
         case 11: m=30;
         break;
         case 12: m=31;
         break;
     }
     date=date+7;
     if(date>m){
         date=date-m;
         if (month==12){
             year++;
             month=1;
         }
         else
         month=month+1;
       
     }
     
     cout << date <<"/"<<month<<"/"<<year<<"\n";
    }
};

int main() {
 Date myObj;
 cout<<"Enter date: ";
 cin>> myObj.date;
 cout<<"Enter month: ";
 cin>>myObj.month;
 cout<<"Enter year: ";
 cin>>myObj.year;
cout << myObj.date <<"/"<<myObj.month<<"/"<<myObj.year<< "\n";
myObj.datechange();

  return 0;
}
