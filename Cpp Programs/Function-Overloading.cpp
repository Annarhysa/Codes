    #include<iostream>
    # define PI 3.142
    using namespace std;
    class Cal{
        private:
        int r,h,a;
        float r1;
        public:
        void Volume(int r,int h)
    {
        cout<<PI*r*r*h;
    }
    void Volume(float r1)
    {
        cout<<(4*PI*r1*r1*r1)/3;
    }
    void Volume(int a)
    {
        cout<<a*a*a;
    }
    void input_display()
    {cout<<"Enter radius and height of a cylinder: ";
    	cin>>r>>h;
    	cout<<" Volume of cylinder is: ";
    	Volume(r,h);
    	cout<<"\nEnter side of cube: ";
    	cin>>a;
    	cout<<" Volume of cube is: ";
    	Volume(a);
        cout<<"\nEnter radius of sphere: ";
    	cin>>r1;
        cout<<"Volume of sphere is: ";
        Volume(r1);}
    };
    int main()
    {Cal cl;
    cl.input_display();
        return 0;
    }
    

