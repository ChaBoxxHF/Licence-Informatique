#include <stdlib.h>
#include <stdio.h>

/*tout a été volé chez axel coézard*/

/*exo 1*/

/*int main(){
  char c;
  while ((c = (char)fgetc(stdin)) != '\n')
    fputc(c, stdout);
}*/

/*exo 2*/

/*int main()
{
	/* CREATION ET ECRITURE */
	/*FILE *f = fopen("mes_caracteres.txt", "w+");
	char c;
	while ((c = (char)fgetc(stdin)) != '\n')
		fputc(c, f);
	fclose(f);*/

	/* LECTURE */
	/*FILE *f_bis = fopen("mes_caracteres.txt", "r+");
	char c_bis;
	while ((c_bis = (char)fgetc(f_bis)) != EOF)
		fputc(c_bis, stdout);
	fclose(f_bis);
}*/

/*exo 3*/

/*int main()
{
	FILE *entree = fopen("entree.txt", "r+");
	FILE *sortie = fopen("sortie.txt", "w+");
	char c_bis;
	while ((c_bis = (char)fgetc(entree)) != EOF)
		fputc(c_bis, sortie);
	fclose(entree);
	fclose(sortie);
}*/

/*exo 4*/

/*#define NBLIGNES 10
#define NBCAR 50

int main()
{
	FILE *texte = fopen("mon_texte.txt", "w+");
	for (int i = 0; i < NBLIGNES; i++)
		fputs("Ceci est une ligne\n", texte);
	fclose(texte);

	FILE *texte_bis = fopen("mon_texte.txt", "r+");
	char c;
	while ((c = (char)fgetc(texte_bis)) != EOF)
		fputc(c, stdout);
	fclose(texte_bis);
}*/

/*exo 5*/

/*axel n'as pas push le 5 sob*/