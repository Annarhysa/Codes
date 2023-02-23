#include <bits/stdc++.h>
using namespace std;
class new_class
{
    public:
    string name;
    int id;

    void printname()
    {
       cout << "Coder Name Is: " << name;}
    
    void coderId()
    {cout<< "Coder ID: "<< id;}
};
  
int main() {
    new_class obj1, obj2;

    obj1.name = "Annarhysa Albert";
    obj2.id = 567890;
    obj1.printname();
    cout << endl;
    obj2.coderId();
    return 0;
}
