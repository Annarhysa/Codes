#include <iostream> 
using namespace std;
 
int main() {
   string str;
   int count = 0, count2 = 0;
   cout<<"Enter a string: ";
   cin>>str;
   char ch;
   for (int index = 0, len = str.length(); index < len; index++) {
      if (str[index]>= '0' && str[index]<='9')
      count2++;
      if (str[index] >= 'a' && str[index] <='z')
      count++;
      if (str[index] >= 'A' && str[index] <='Z')
      count++;
   }
 
   cout <<"Number of letters: "<<count<< endl;
   cout<<"Number of digits: "<<count2<<endl;
}
