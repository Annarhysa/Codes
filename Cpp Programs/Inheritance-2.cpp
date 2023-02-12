// C++ program to calculate the area of a square and a circle

#include <iostream>
using namespace std;

// Abstract class
class Shape {
   protected:
    float d1, d2, r;

   public:
    void getSquare_Circle() {
        cin >> d1;}
    void getRect(){
        cin>>d1;
        cin>>d2;
    }

    // pure virtual Function
    virtual float calculateArea() = 0;
};

// Derived class
class Square : public Shape {
   public:
    float calculateArea() {
        return d1 * d1;
    }
};

// Derived class
class Circle : public Shape {
   public:
    float calculateArea() {
        return 3.14 * d1 * d1;
    }
};

class Rectangle: public Shape{
    public:
    float calculateArea(){
    return d1*d2;
}};
int main() {
    Square square;
    Circle circle;
    Rectangle rec;

    cout << "Enter the length of the square: ";
    square.getSquare_Circle();
    cout << "Area of square: " << square.calculateArea() << endl;

    cout << "\nEnter radius of the circle: ";
    circle.getSquare_Circle();
    cout << "Area of circle: " << circle.calculateArea() << endl;
    
    cout << "\nEnter the length and breadth of the Rectangle: ";
    rec.getRect();
    cout << "Area of rectangle: " << rec.calculateArea() << endl;


    return 0;
}
