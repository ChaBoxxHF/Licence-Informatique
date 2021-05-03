#define LECTURE    /* A COMPLETER */
#define ECRITURE   /* A COMPLETER */
#define EXECUTION  /* A COMPLETER */
typedef int droits;
void afficheDroit(droits D) {
  if (/* A COMPLETER */) printf("r");
     else printf("-");
  if (/* A COMPLETER */) printf("w");
     else printf("-");
  if (/* A COMPLETER */) printf("x");
     else printf("-");
  printf("\n");
}
 
int main(int argc, char **argv) {
  /* Affiche les droits en lecture seule */
  afficheDroit(/* A COMPLETER */);
 
  /* Affiche les droits en lecture et execution */
  afficheDroit(/* A COMPLETER */);
 
  /* Affiche les droits passes en parametre */
  if (argc > 1) afficheDroit(atoi(argv[1]));
}

#include <stdio.h>
#include <stdlib.h>
 
#define LECTURE   2 
#define ECRITURE  4 
#define EXECUTION 8
 
typedef int droits;
 
void afficheDroit(droits D)
{
  if (D&LECTURE) printf("r"); else printf("-");
  if (D&ECRITURE) printf("w"); else printf("-");
  if (D&EXECUTION) printf("x"); else printf("-");
  printf("\n");
}
 
int main(int argc, char **argv)
{
  /* Affiche les droits en lecture seules */
  afficheDroit(LECTURE);
  /* Affiche les droits en lecture et execution */
  afficheDroit(LECTURE|EXECUTION);
 
  /* Affiche les droits passes en parametres */
  if (argc > 1) afficheDroit(atoi(argv[1]));
  exit(0);
}