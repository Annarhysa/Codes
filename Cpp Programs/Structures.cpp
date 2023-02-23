#include <iostream>
using namespace std;
 
struct Employee {
    char name[100];
    int salary;
    int empCode;
    char dep[200];
};
 
int main() {
    Employee e;
     
    cout << "Enter the Name of Employee : ";
    cin.getline(e.name, 100);
    cout << "Enter the Department : ";
    cin.getline(e.dep, 200);
    cout << "Enter the Salary of Employee : ";
    cin>>e.salary;
    cout << "Enter the Employee Code : ";
    cin>>e.empCode;
     
    cout << "\n\tEmployee Details\t" << endl;
    cout << "Name : " << e.name <<endl;
    cout<< "Department : " << e.dep<<endl;
    cout<< "Salary : " << e.salary <<endl;
    cout << "Employee Code : " << e.empCode << endl;
    return 0;
}
