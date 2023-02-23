#include <iostream>

using namespace std;
int swap (int *a, int *b);
int main()
{
int a, b;
cout<<"Enter the two numbers that has to be swapped: ";
cin>>a>>b;
cout<<"Before swap a = "<<a<<" and b = "<<b<<endl;
swap(&a,&b);
cout<<"After swap a = "<<a<<" and b = "<<b<<endl;;
    return 0;
}

int swap(int *a, int *b)
{int temp;
temp = *a;
*a = *b;
*b = temp;
return(*a,*b);}
