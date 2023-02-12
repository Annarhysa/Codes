// Example:

#include<iostream>
using namespace std;

class Student
{

	public:
	
	int a, b, c;
		void sub()
		{cout<<"Enter the Grade points out of 10"<<endl;
			cout<<"In Subject A :";
			cin>>a;
			
			cout<<"In Subject B :";
			cin>>b;
			
			cout<<"In Subject C :";
			cin>>c;
		}
		void disp()
		{
			cout<<endl<<"Grades in Subject A :"<<a;
			
			cout<<endl<<"Grades in Subject B :"<<b;
			
			cout<<endl<<"Grades in Subject C :"<<c<<endl;
			
		}};


class Grading_System: public Student
{	public:
		void cal_CGPA()
		{sub();
		disp();
		cout<<"The CGPA is: "<<(a+b+c)/3;
		}
		
};

class Faculty: private Grading_System
{ public:
void show(){
cal_CGPA();}};

int main()
{
	
	Grading_System obj; 
	obj.cal_CGPA();
	
	return 0;
	
}
