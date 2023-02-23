#include <stdio.h>
#include <stdlib.h>
int main()
{
    int no1, no2, s;
    printf("Enter A Digit: ");
    scanf("%d", &no1);
    printf("Enter Another Digit: ");
    scanf("%d", &no2);
    
    if (no1>no2)
    s = no1-no2;
    else
    s = no2-no1;
    printf("Difference of The Given Digits = %d", s);
    return 0;
}
