#include<stdio.h>
int main() {
long int x;
int a = 1 , b , var, n, c, k, q;
char hexanum_decimal[ 100 ];
scanf("%d %d", &n, &q);
  switch(q){
      case 0:
      printf("%d", n);
      for (c = 31; c >= 0; c--)
      {
          k = n >> c;
          if (k & 1)
          printf("1");
          else
          printf("0");
          
      }
      break;
      case 1:
      x = n ;
      while( x != 0 ) {
          var = x % 16 ;
          if( var < 10 )
          var = var + 48 ;
          else
          var = var + 55 ;
          hexanum_decimal[ a++ ]= var ;
          x= x / 16;
          
      }
      for ( b = a -1 ; b > 0 ; b-- )
      printf( "%c" , hexanum_decimal[ b ] ) ;
      break;
  }
      return 0 ;
}
