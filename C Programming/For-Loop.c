#include <stdio.h>

int main()
{
int i,n,sum=0;
printf("Enter The Value of n: \n");
scanf("%d",&n);
for (i=1; i<=n; i++)
{
    sum=sum+i;
}
printf("The Sum of n Numbers Is: %d",sum);
return 0;
}
