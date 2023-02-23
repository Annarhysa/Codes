#include <stdio.h>

int main()
{
    int i;
    char c;
    char ch[10];
    float f;
    printf("Please Enter A Character= ");
    scanf("%c", &c);
    printf("Please Enter A String= ");
    scanf("%s", ch);
    printf("Please Enter An Integer= ");
    scanf("%d", &i);
    printf("Please Enter A Decimal= ");
    scanf("%f", &f);
    
    printf("\n The Integer That You Entered= %d", i);
    printf("\n The Character That You Entered= %c", c);
    printf("\n The String That You Entered= %s", ch);
    printf("\n The Decimal That You Entered= %f", f);
    printf("\n The Decimal Value With Precision 2= %.2f", f);

    return 0;
}

