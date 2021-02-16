#include <stdio.h>
#include <stdlib.h>
#include <time.h>

 
int main()
{
   int e;
   printf("choisissez un nombre maximal d'entité: e=");
   scanf("%d",&e);
   srand(time(NULL)); // Initialisation de la donnée seed
   printf("%d\n", rand()%e); // rand  renvoie un nombre calculé à partir de la donnée seed
   return 0;
}