#include <iostream>

using namespace std;

int main()
{
   int sum=0,a[50];
   cout<<"Enter an array of 50 elements: "<<endl;
   for (int i=1;i<=50;i++){
       cin>>a[i];
       if(a[i]<0)
       {break;}
       else if(a[i]>=0 && a[i]<=50){
        cout<<"\nIt is a positive integer"<<endl; }
        else
        {continue;}
       }
       
   
    return 0;
}
