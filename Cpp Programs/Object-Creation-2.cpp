#include <iostream>

using namespace std;
class Student {      
  public:            
    int roll_no;        
    string name;  
};

int main() {
  Student myObj;  

  myObj.roll_no = 2;
  myObj.name = "John";

  cout <<"Name: "<< myObj.name<< "\n";
  cout <<"Roll No.: "<< myObj.roll_no ;
  
  return 0;
}
