#include <stdio.h>
int main()
{
    char c = 'A', a[] = "gdbonlinecompiler", s[20], ch;
    int x = 4, y = 5, z = 7, b = 0, d = 0, e = 0;
    float f = 3.69;
    double g = 0.0;
    //Character format specifier
    printf("%c\n", c); 
    
    //integer format specifier
    printf("%d\n", x); 
    printf("%i\n", y);
   
    //Unsigned Integer Format Specifier
    printf("%u\n", -10); // The -10 value is converted into it's positive
    printf("%u\n", 10);  

    //Floating-point format specifier
    printf("%f\n", f);
    printf("%e\n", f);
    
    //Unsigned Octal number for integer
    printf("%o\n", z);
 
    //String printing
    printf("%s\n", a);
  
    //Address Printing
    printf("The Memory Address of z = %p\n", (void*)&z);
    
    //More formatting
    printf("%20s\n", a);
    printf("%-20s\n", a);
    printf("%20.5s\n", a);
    printf("%-20.5s\n", a);
    
    //Scanf
    printf("Enter A Value = ");
    scanf("%d", &b);
    printf("%d\n", b);
    
    //Integer may be octal or in hexadecimal
    printf("Enter A Value = ");
    scanf("%i", &d); // input is 017 (octal of 15 )
    printf("%d\n", d);
    printf("Enter A Value = ");
    scanf("%i", &e); // input is 0xf (hexadecimal of 15 )
    printf("%d\n", e);
    
    //Double floating-point number
    printf("Enter A Value = ");
    scanf("%lf", &g);
    printf("%lf\n", g);
    
    //String input 
    printf("Enter A String = ");
    scanf("%s", s); 
    printf("%s\n", s);
    
    //Charachter input
    printf("Enter A Charachter = ");
    ch = getchar();
    printf("%c\n", ch);
    return 0;
}
