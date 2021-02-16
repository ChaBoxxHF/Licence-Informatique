#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <gmp.h>

long puissance (long a, long e, long n);

int main()
{
  long a, e, n;
  printf("Entrer les nombres a, e et n\n");
  printf("a= ");
  scanf("%ld", &a);
  printf("e= ");
  scanf("%ld", &e);
  printf("n= ");
  scanf("%ld", &n);
  printf("expo modulaire carre= %ld \n", puissance (a,e,n));
}


long puissance (long a, long e, long n) 
{  
  long p;
  for (p = 1; e > 0; e = e / 2) {
    if (e % 2 != 0)
      p = (p * a) % n;
    a = (a * a) % n;
  }
  return p;
}