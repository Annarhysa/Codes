#include<iostream>
using namespace std;
class Reverse
{
	private:
		int i;
		public:
	Reverse(int n)
	{
		
		cout<<endl<<"The reverse of the Entered number: ";
		for(i=n;n>0;n=n/10)
		{
			cout<<n%10;
		}
	}
	Reverse(long int a)
	{
		cout<<endl<<"The reverse of the Entered number: ";
		for(i=a;a>0;a=a/10)
		{
			cout<<a%10;
		}
	}
};
int main()
{
	int choice;
	cout<<"Choice 1: Reverse a number"<<"\n"<<"Choice 2: Reverse a string"<<endl;
	cout<<"Enter choice: ";
	cin>>choice;
	switch(choice)
	{
		case 0:
		{
			int n;
			cout<<"Enter a number to Display: ";
			cin>>n;
			Reverse r(n);
			break;
		}
		case 1:
			{
			 long int a ;
			 cout<<"Enter  Number to Display: ";
			 cin>>a;
			 Reverse r(a);
		     break;
		   }
				default:
					cout<<"Invilide Choice:";
				
	}
}
