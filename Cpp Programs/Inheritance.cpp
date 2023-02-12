#include <iostream>
using namespace std;
class Marks{
    virtual void getpercentage()=0;
};
class A:public Marks{
    public:
    int sub1,sub2,sub3;
    double aper;
    A(int a,int b,int c){
        sub1=a;
        sub2=b;
        sub3=c;
    }
    void getpercentage(){
        aper=(sub1+sub2+sub3)/3;
        cout<<"Percentage of Student A is:"<<aper<<endl;
    }
};
class B:public Marks{
    public:
    int sub1,sub2,sub3,sub4;
    double bper;
    B(int a,int b,int c,int d){
        sub1=a;
        sub2=b;
        sub3=c;
        sub4=d;
    }
    void getpercentage(){
        bper=(sub1+sub2+sub3+sub4)/4;
        cout<<"Percentage of Student B is:"<<bper<<endl;
    }
};
int main(){

    A student(90,90,90);
    student.getpercentage();
    B student2(80,80,80,80);
    student2.getpercentage();
    return 0;}
