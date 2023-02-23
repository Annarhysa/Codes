#include <stdio.h>

int main()
{int arr[10];
int i, min, max;
for(i=0; i<10; i++)
{printf("Enter a value: ");
scanf("%d", &arr[i]);}
min = arr[0];
max = arr[0];
for(i=0; i<10; i++){
    if(arr[i]>max)
    max = arr[i];
    if(arr[i]<min)
    min = arr[i];}
    printf("The max and min elements are: %d%d", max,min);
    return 0;
}
