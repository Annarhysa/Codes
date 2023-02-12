#include <iostream>
using namespace std;

template <class T>
class Number{
    T num;
    public:
Number(T n1, T n2){
        num=(n1 > n2) ? n1 : n2;
       
}
 ~Number()    
        {    
            cout<<num;    
        }
};
int main()
{
        Number<int> numberInt(5, 6);
       
       
        return 0;
}
