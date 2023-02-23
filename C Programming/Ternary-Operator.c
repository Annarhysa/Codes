#include <stdio.h>

int main()
{int a,b,c;
    printf("Give Two Numbers: ");
    scanf("%d %d", &a, &b);
    c = (a>b)?a:b;
    printf("The biggest value: %d", c);
    return 0;
}

