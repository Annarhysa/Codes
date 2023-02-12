#include<iostream>
using namespace std;
class Vehicle {
public:
	void output()
	{
	cout << "This is a Vehicle\n";
	cout<<" "<<endl;
	}
};
class Two_Wheeler : public Vehicle {
    public:
    void disp(){
        output();
    cout<<"A Two Wheeler Vehicle"<<endl;
        cout<<""<<endl;
    }

};

class Four_Wheeler : public Vehicle{
    public: 
    void show(){
        output();
    cout<<"A Four Wheeler Vehicle"<<endl;}
};

class Car: public Four_Wheeler{
    public:
    void show_1(){
        show();
        cout<<"I am specifically a car"<<endl;   }
    };
    
    int main()
{Two_Wheeler obj;
	Car obj1;
	obj.disp();
	obj1.show_1();
	return 0;
}
