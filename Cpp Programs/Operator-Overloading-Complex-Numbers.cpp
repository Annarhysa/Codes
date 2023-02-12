#include<iostream>
#include<conio.h>
using namespace std;
class complex {
    int a, b;
public:

    void getvalue() {
        cout << "Enter the value of Complex Numbers a,b:";
        cin >> a>>b;
    }

    complex operator+(complex ob) {
        complex t;
        t.a = a + ob.a;
        t.b = b + ob.b;
        return (t);
    }

    complex operator-(complex ob) {
        complex t;
        t.a = a - ob.a;
        t.b = b - ob.b;
        return (t);
    }

    void display() {
        cout << a << "+(" << b << ")i" << "\n";
    }
};

int main() {
    complex obj1, obj2, result, result1;

    obj1.getvalue();
    result = obj1 + obj2;
    cout << "Input Values:\n";
    obj1.display();
    cout << "Result:";
    result.display();
    
    obj2.getvalue();
    result1 = obj1 - obj2;
    cout << "Input Values:\n";
    obj2.display();
    result1.display();

    getch();
}
