#include <iostream>
#include <string>
using namespace std;

class student
{
    int roll;
    string name;
    char grade[50];
public:
    void getInfo(){
        cout<<"Enter Roll No.: ";
        cin>>roll;
        cout<<"Enter Name: ";
        cin>>name;
        cout<<"Enter Grade: ";
        cin>>grade;
    }
    void showInfo(){
        cout<<"Roll Number : "<<roll<<endl;
        cout<<"Name : "<<name<<endl;
        cout<<"Grade : "<<grade<<endl;
    }
};

class display : private student
{
public:
    void getData(){
        cout<<"Enter student data: \n";
        getInfo();
    }
    void showData(){
        cout<<"\nStudent data as follows "<<endl;
        showInfo();
    }
};
int main(){
    display obj1;
    obj1.getData();
    obj1.showData();
    return 0;
}
