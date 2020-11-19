#include <stdio.h>
#include <stdlib.h>
#include <time.h>

 
int main()
{
   srand(time(NULL)); // Initialisation de la donnée seed
   printf("%d", rand()%50); // rand  renvoie un nombre calculé à partir de la donnée seed

   return 0;
}