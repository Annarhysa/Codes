#include <stdio.h>
int main()
 {
 int i ;
 float x[10], value, total;
 /* . . . . . .READING VALUES INTO ARRAY . . . . . . */
 printf("Enter 10 Real Number \n") ;
 for( i = 0 ; i < 10 ; i++ )
 {
 scanf("%f", &value) ;
 x[i] = value ;
 }
 /* . . . . . . .COMPUTATION OF TOTAL . . . . . . .*/
 total = 0.0 ;
 for( i = 0 ; i < 10 ; i++ )
 total = total + x[i] * x[i] ;
 /*. . . . PRINTING OF x[i] VALUES AND TOTAL . . . */
 printf("\n");
 for( i = 0 ; i < 10 ; i++ )
 printf("x[%2d] = %5.2f\n", i+1, x[i]) ;
 printf("\ntotal = %.2f\n", total) ;
 }
