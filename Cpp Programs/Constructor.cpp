#include <iostream>
#include <string>
using namespace std;
class Pyramid{
    int i,j,spc,rows,k;
    
    public:
    Pyramid(){
        cout << "\n\n Display such a pattern like a pyramid using number with repetition :\n";
        cout << "-------------------------------------------------------------------------\n";
        cout << " Input number of rows: ";
        cin >> rows;
        spc=rows+4-1;}
        void pattern(){
        for(i=1;i<=rows;i++)
        {
            for(k=spc;k>=1;k--)
            {
                cout<<" ";
            }
	   for(j=1;j<=i;j++){
	       cout<<i<<" ";}
	   cout<<endl;
       spc--;}}};
int main()
{Pyramid p;
p.pattern();
return 0;}
