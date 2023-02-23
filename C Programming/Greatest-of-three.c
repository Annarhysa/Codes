int main()
{int a,b,c;
printf("Enter value of a: ");
scanf("%d", &a);
printf("Enter value of b: ");
scanf("%d", &b);
printf("Enter value of c: ");
scanf("%d", &c);
if (a>b)
{if (a>c) {printf("Greatest No.: %d\n", a);}}
else if (b>a)
{if (b>c) {printf("Greatest No.: %d\n", b);}}
else if (c>a)
{if (c>b) {printf("Greatest No.: %d\n", c);}}
else
{printf("All are equal\n");}
printf("End of the Program");
    return 0;
}
