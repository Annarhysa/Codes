#include <iostream>
using namespace std;

template <class T>
inline T square(T x)
{
   T result;
   result = x * x;
   return result;
};
int main()
{
   int    i, ii;
   float  x, xx;
   double y, yy;

   i = 2;
   x = 2.2567;
   y = 2.2;

   ii = square<int>(i);
   cout << "Square of integer "<< i << " is " << ii << endl;

   xx = square<float>(x);
   cout << "Square of float "<< x << " is " << xx << endl;

   yy = square<double>(y);
   cout << "Square of double "<< y << " is " << yy << endl;

   yy = square(y);
   cout<<"\nShowing implicit use of the template:\n";
   cout << y << ": " << yy << endl;
   return 0;}
