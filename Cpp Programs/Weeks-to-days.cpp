#include <iostream>

using namespace std;

int main()
{
    int daysTravelled, weeks, days;
    cout<<"Enter the number of days travelled: "<<endl;
    cin>>daysTravelled;
    
    weeks = daysTravelled/7;
    days = daysTravelled%7;
    
    cout<<daysTravelled<<" days are "<<weeks<<" weeks and "<<days<<" remaining days "<<endl;

    return 0;
}
