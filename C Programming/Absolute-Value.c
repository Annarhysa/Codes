#include <stdio.h>
#include <stdlib.h>
int main()
{
    int no1, no2;
    printf("Enter A Digit: ");
    scanf("%d", &no1);
    printf("Enter Another Digit: ");
    scanf("%d", &no2);
    printf("Difference of The Given Digits = %d", abs(no1-no2));
    return 0;
}
