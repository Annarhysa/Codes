#include<iostream>
 using namespace std;
 int s = 0;
 int sum(int x)
 { while (x != 0) {
      s = s + x % 10;
      x = x / 10;
   }return (s);
 }
 long int sum(long int y)

 { while (y != 0) {
      s = s + y % 10;
      y = y / 10;
 }return s;}

 
 int main()
 {
     cout <<"The Sum of two integers: "<<sum(10)<<endl;
     cout <<"The Sum of two floats: "<<sum(109876)<<endl;
 }     
