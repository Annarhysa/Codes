#include <iostream>
#include <string>
using namespace std;

class employee1
{
    string name;
    int employee1ID, age;
public:
    void getData1(){
        cout<<"Enter Name: ";
        cin>>name;
        cout<<"Enter Employee ID: ";
        cin>>employee1ID;
        cout<<"Enter Age: ";
        cin>>age;
    }
    void showData1(){
        cout<<"Employee name : "<<name<<endl;
        cout<<"Employee ID : "<<employee1ID<<endl;
        cout<<"Employee age : "<<age<<endl;
    }
};

class employee2
{
    string name;
    int employee2ID, age;
public:
    void getData2(){
         cout<<"Enter Name: ";
        cin>>name;
        cout<<"Enter Employee ID: ";
        cin>>employee2ID;
        cout<<"Enter Age: ";
        cin>>age;
    }
void showData2(){
        cout<<"Employee name : "<<name<<endl;
        cout<<"Employee ID : "<<employee2ID<<endl;
        cout<<"Employee age : "<<age<<endl;
    }
};

class display : private employee1, private employee2
{
public:
    void getData(){
        cout<<"Enter details for employee 1 : \n";
        getData1();
        cout<<"Enter details for employee 2 : \n";
        getData2();
    }
    void showData(){
        cout<<"\nDetails of employee 1 : \n";
        showData1();
        cout<<"\nDetails of employee 2 : \n";
        showData2();
    }
};

int main() {
    // insert code here...
    display obj1;
    obj1.getData();
    obj1.showData();
    return 0;}

