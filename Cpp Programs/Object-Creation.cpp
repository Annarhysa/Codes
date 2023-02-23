#include<iostream>
using namespace std;

class Swap

{private:

int a,b, temp = 0;

float m,n,temp1 = 0;

public:
void display(int a,int b)

{
temp = a;
a=b;

b=temp;

cout<<"After swapping integer values are: a = "<<a<<" b = "<<b<<endl;

}
void display(float m, float n)
{temp1 = m;
m=n;

n=temp1;

cout<<"After swapping float values are: m = "<<m<<" n = "<<n<<endl;}
void input()

{

cout<<"Enter any two integers: ";

cin>>a>>b;

cout<<"Before swapping integer values are: a = "<<a<<" b = "<<b<<endl;

display(a,b);
cout<<"Enter any two float values: ";

cin>>m>>n;

cout<<"Before swapping float values are: m = "<<m<<" n = "<<n<<endl;
display(m,n);

}


};

int main()

{Swap s1;
s1.input();
return 0;

}
