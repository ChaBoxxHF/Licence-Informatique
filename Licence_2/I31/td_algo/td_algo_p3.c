#include <stdio.h>

/*exo 98-99*/

/*int main()
{
	const int N = 5;
	int nombres[N];
	int tmp;

	printf("Entrer un 1er nombre: ");
	scanf("%d", &nombres[0]);
	for (int i = 1; i < N; i++)
	{
		printf("Entrer un %dème nombre: ", i);
		scanf("%d", &tmp);

		if (nombres[i - 1] > tmp)
		{
			nombres[i] = nombres[i - 1];
			nombres[i - 1] = tmp;
			continue;
		}
		nombres[i] = tmp;
	}

	for (int i = 0; i < N; i++)
		printf("%d\n", nombres[i]);
}*/

/*exo 99 corrigé*/

/*int main(){
    const int N = 5;
    int nombres[N];
    for (int i = 0; i < N; i++){
        printf("Entrer un nombre: ");
    scanf("%d", &nombres[i]);
    }
    for (int i = N-1; i >=0; i--)
        printf("%d\n", nombres[i]);
}*/

/*exo 100*/

/*int main()
{
	const int N = 10;
	const int x = 5;
	int A[] = {0, 1, 5, 3, 4, 5, 6, 7, 8, 5};

	for (int i = 0; i < N; i++)
		if (A[i] == x)
			printf("A[%d] = %d\n", i, x);
}*/

/*exo 101*/


/*int main()
{
	int N = 10, x = 5;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

	int isFind = 0;
	for (int i = 0; i < N; i++)
		if (isFind || A[i] == x)
		{
			isFind = 1;
			A[i] = A[i + 1];
		}
	if (isFind)
		N--;

	for (int i = 0; i < N; i++)
		printf("%d\n", A[i]);
}*/

/*exo 101 corrigé*/


/*#define N 10
int main(){
    int A[N]={2,4,1,9,9,5,6,7,1,6};
    int i, x, j;
    int c=0;
    printf("Entrer x: ");
    scanf("%d", &x);
    for(i=0;i<N;i++){
    if(A[i]==x){
        c++;
        for(j=i;j<N-1;j++)
            A[j]=A[j+1];
            i--;
    }
    }
    for (i = 0; i < N-c; i++)
        printf("%d ", A[i]);
        printf("\n");
}*/


/*exo 102*/

/*int main(){
    int N = 10, x = 5;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    int x;
    int i=0;
    printf("entrez un nombre entre 0 et 9\n");
    scanf("%d",&x);
    do{

    } while (!=x)
}*/

/*correction*/

/*#define N 5

int main(){
	int A[N]={2,3,4,5,6};
	int g=0,d=N-1, m=(g+d)/2;
	int x,i;
	printf("saisir nb:");
	scanf("%d",&x);
	while (x!=A[m] && d-g>=0){
		if (x>A[m]){
			g=m+1;
			m=(g+d)/2;
		}
		else{
			d=m-1;
			m=(d+g)/2;
		}
	}
	if (x==A[m]){
		printf("%d  est à la position %d\n",x,m);
	}
	else{
		printf("%d n'est pas dans le tableau\n",x);
	}
}*/

/*exo 103*/

/*solution 1*/

/*#include <stdio.h>

#define N 10

int main()
{
  int vecteurs[2][N] = {{-1, 2, 3, 5, 2, 8, -3, 9, 7, 6},
                        {2, 3, 8, 9, 7, 1, -4, -5, 6, 9}};

  int prod_scal = 0;
  for (int i = 0; i < N; i++)
    prod_scal += vecteurs[0][i] * vecteurs[1][i];

  printf("%d\n", prod_scal);
}*/

/*SOLUTION 2*/

/*#include <stdio.h>

#define N 10

int main()
{
  int A[N] = {-1, 2, 3, 5, 2, 8, -3, 9, 7, 6};
  int B[N] = {2, 3, 8, 9, 7, 1, -4, -5, 6, 9};

  int prod_scal = 0;
  for (int i = 0; i < N; i++)
    prod_scal += A[i] * B[i];

  printf("%d\n", prod_scal);
}*/

/*exo 104*/

/*#define N 10
int main()
{
	int tab1[N]={1,2,4,7,9,12,23,45,67,90};
	int tab2[N+1];
	int i,j,x;
	printf(" Entrer le nombre à insérer : "); 
	scanf("%d ", &x);
	while (tab1[i] <x){
		tab2[i] ==tab1[i];
		i++;
	}
	if (tab1[i]==x)
 		printf(" l’élément est déjà dans le tableau ");
	else 
	{
		tab2[i]=x;
		for (j=i+1;j<N+1;j++)
 		tab2[j]=tab1[j-1];

		printf("affichage du tableau");
		for (i=0;i<N+1;i++)
 		printf(" %d " , tab2[i]);

}
}*/

/*exo 105*/

/*int i;
int *p;
i=1;
p=&i;
printf("%d",i);
*p=4;
printf("%d",*p);*/


/*exo 111*/

void carre(int *x){
	*x *= *x;
}

/*int main(){
	int x;
	printf("donnez une valeur");
	scanf("%d",&x);
	carre(&x);
	printf("le carré de x =%d",x);
}*/

/*exo 112*/

void echange(int *x,int *y){
	int tmp = *y;
	*y = *x;
	*x=tmp;
}

/*int main(){
	int x,y;
	printf("\nEntrez deux nombres:");
	scanf("%d %d",&x,&y);
	printf("\n avant echange x=%d,y=%d",x,y);
	echange(&x,&y);
	printf("\naprès echange x=%d, y=%d",x,y);
}*/

/*exo 116*/

void changeSigne(int *tab, int taille)
{
    for (int i = 0; i < taille; i++)
        tab[i] = -tab[i];
}

/*int main(){
	
}*/

int moyenne(int *tab, int taille)
{
    int moyenne = 0;
    for (int i = 0; i < taille; i++)
        moyenne += tab[i];
    return moyenne / taille;
}

/*int main(){

}*/


/*exo 118*/

/*void miroir(int *tab, int taille){
    int tmp;
	int j=taille;
    for (int i=0; i<taille/2;i++)
        tmp=tab[i];
        tab[i]=tab[j];
        tab[j]=tmp;
    }
}*/

/*exo 119*/

#define N 10

int rechercheseq(int T[],int x){
	int i=0;
	while ((T[i]!=x)&&(i<N)){
		i++;
	}
	if (i==N){
		return -1;
	}
	else return i;
}

/*int main(){
	int tab[N]={};
	int i,x,res;
	printf("entrer les 10 éléments du tableau:");
	for (i=0;i<N;i++){
		scanf("%d",&tab[i]);
	}
	printf("entrer l'élément recherché");
	scanf("%d",&x);
	res=rechercheseq(tab,x);
	if (res==-1){
		printf("%d n'existe pas dans le tableau\n",x);}
	else{
		printf("%d a été trouvé à l'indice %d du tableau\n",x,res);
	}
}*/

/*exo 122*/

/*#define N 5
#define M 3

void lecture(int T[M][N], int x, int y){
	printf("l'élément %d %d : %d",x,y,T[x][y]);
}

void modification(int T[M][N], int x, int y){
	T[x][y]++;
}

void affiche(int T[M][N]){
	int i,j;
	printf("\n");
	for (i=0;i<M;i++){
		for (j=0;j<N;j++){
			printf("%d\t",T[i][j]);
			print("\n");
		}
	}
}

void permuteligne(int T[M][N], int i, int j){
	int tmp;
	for (int=0;k<N;k++){
		tmp=T[i][k];
		T[i][k]=T[k][j];
		T[k][j]=tmp;
	}
}

void permutecol(int T[M][N], int i, int j){
	int tmp;
	for (int k=0;k<M;k++){
		tmp= T[k][i];
		T[k][i]=T[k][j];
		T[k][j]=tmp;
	}
}

int somme(int T[M][N]){
	int i,j,s=0;
	for (i=0;i<M;i++){
		for (j=0;j<N;j++){
			s+=T[i][j];
		}
	}
	return s;
}

int sommecontour(int T[M][N]){
	int s=0
	for (int j=0;j<N;j++){
		s+=T[0][j];
		s+=T[M-1][j];
	}
	for (int i=1;i<M-1;i++){
		s+=T[i][0];
		s+=T[i][N-1];
	}
	return s;
}*/

int nbchar(char tab[]){
	int c=0;
	while (tab[c]!="\0"){
		c++;
	}
	return c;
}

int estpalindrome(char tab[],int n){
	int i=0;
	while ((i<n/2)&(tab[i]==tab[n-1-i])){
		i++;
	}
	return (i==n/2);
}

int main(){
	char tab[]="radar";
	int s=nbchar(tab);
	if (estpalindrome(tab,s)){
		printf("%s est un palindrome\n",tab);
	}
	else{
		printf("%s n'est pas un palindrome\n",tab);
	}
}