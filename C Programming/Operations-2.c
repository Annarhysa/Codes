#include <stdio.h>
#include <stdlib.h>
int main()
{
    float no1, no2;
    printf("Enter A Digit: ");
    scanf("%f", &no1);
    printf("Enter Another Digit: ");
    scanf("%f", &no2);
    printf("\nSum= %f", no1+no2);
    printf("\nDifference= %d", abs(no1-no2));
    printf("\nProduct= %f", no1*no2);
    printf("\nDivison= %f", no1/no2);
    return 0;
}
