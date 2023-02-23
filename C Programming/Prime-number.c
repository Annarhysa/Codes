#include <stdio.h>

int
main ()
{
  int a, b, i, c = 1;
  printf ("Enter the start and end no.'s of the list : ");
  scanf ("%d%d", &a, &b);
  for (i = a; i <= b; i++)
    {
      for (int j = 2; j <= b; j++)
	{
	  if ((i % j) == 0)
	    {
	      c = 0;
	    }
      if (c == 1)
	{
	  printf ("%d\n", i);
	}
    }
  return 0;
}
