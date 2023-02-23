#include<iostream>
using namespace std;

int fibonacci(int n)
{
if(n<=1)
  return n;
return fibonacci(n-1)+fibonacci(n-2);
}

int main()
{
int n,i=0;
cout<<"Enter the value of n: ";
cin>>n;
while(i<n)
{
cout<<fibonacci(i)<<"\n";
i++;
}
return 0;
}
