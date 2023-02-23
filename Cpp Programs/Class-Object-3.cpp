#include <iostream>
#include<cstring>

using namespace std;
class Student {      
  public:            
    char name[50];
    char ch;
    void get_Str(){
        cin.getline(name,50);}
    void print_Str(){
        for (int i = 0; i < strlen(name); i++) {
            ch = toupper(name[i]);
            cout<<ch;}
            cout<<endl;
        for (int i = 0; i < strlen(name); i++) {
            ch = tolower(name[i]);
            cout<<ch;}}};

int main() {
  Student myObj;
  myObj.get_Str();
  myObj.print_Str();

  return 0;
}

