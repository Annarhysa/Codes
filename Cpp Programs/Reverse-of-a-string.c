#include <iostream> 
using namespace std;
string reverse(string str);
int main() {
   string str;
   cout<<"Enter a string: ";
   cin>>str;
   cout<<"The reverse of the string: "<<reverse(str)<<endl;
   return 0;}

string reverse(string str)
{
   char ch;
   for (int index = 0, len = str.length(); index < len/2; index++) {
      ch = str[index];
      str[index] = str[len-1-index];
      str[len-1-index] = ch;
   }
   return (str);
}
