#include <iostream>
#define PI 3.142
using namespace std;

class Circle {
    public:
    double radius;
   
    void a()
    {cout<<"The Radius: "<<radius<<endl;
    cout<<"The Area: "<<PI*radius*radius<<endl;
        cout<<"The Circumference: "<<PI*2*radius<<endl;
    }
};

int main () {
    Circle area;
    area.radius = 4;
    area.a();
  return 0;
}
