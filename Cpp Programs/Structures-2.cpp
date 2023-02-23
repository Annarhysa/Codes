#include <iostream>
using namespace std;
 
struct Distance{
    int feet1;
    int feet2;
    int inch1;
    int inch2;
    int fsum=0;
    int isum=0;
};
 
int main() {
    Distance d;
    cout<<"Enter 1st distance in feet and inches"<<endl;
    cin>>d.feet1>>d.inch1;
    cout<<"\nEnter 2nd distance in feet and inches"<<endl;
    cin>>d.feet2>>d.inch2;  
    d.fsum=d.feet1+d.feet2;
    d.isum=d.inch1+d.inch2;
    if(d.isum>=12){
        d.fsum++;
        d.isum=d.isum-1;
    }
   cout<<"sum of given distance: "<<d.fsum<<"'"<<d.isum<<"''"<<endl;
    return 0;
}
