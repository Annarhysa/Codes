#include <stdio.h>

int main()
{
    int b = 10;
    
    printf("Initial Number = %d\n", b);
    
    b += 1;
    printf("The Value of Given Number After Increment = %d\n", b);
    
    b -= 1;
    printf("The Value of Given Number After Decrement= %d\n", b);
    
    b *= b;
    printf("The Value of Given Number After Multiplicative Increment= %d\n", b);
    
    b /=b;
    printf("The Value of Given Number After Divisional Decrement= %d\n", b);
    
    return 0;
}
