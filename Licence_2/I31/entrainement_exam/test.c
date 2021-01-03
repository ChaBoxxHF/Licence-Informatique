#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*exo 1*/

// int main(){
//     printf("Hello \nWorld\n");
// }

/*exo 4*/

// int main(){int main(){
//     int x;
//     do{
//         printf("entrez un nombre positif: ");
//         scanf("%d",&x);
//     } while (x<0);
//     printf("%d\n",x);
// }
//     const int pi=3.14159;
//     int a=pi;
//     printf("%d\n",a);
// }

/*exo 28*/

// int main(){
//     int n;
//     printf("entrez un nombre n: ");
//     scanf("%d",&n);
//     if (n<0){
//         printf("-1\n");
//     }
//     else if (n==0){
//         printf("0\n");
//     }
//     else{
//         printf("1\n");
//     }
// }

/*exo 41*/

// int main(){
//     printf("entrez un nombre pour x: ");
//     int x;
//     scanf("%d",&x);
//     printf("%d au carré donne: %d\n",x,x*x);
// }

/*exo 43*/

// int main(){
//     printf("entrez la longueur d'un coté d'un carré: ");
//     int x;
//     scanf("%d",&x);
//     printf("la diagonale d'un carré de longueur %d est %d",x,sqrt((x*x)+(x*x)));
// }

/*exo 44*/

// int main(){
//     int x;
//     do {
//         printf("Veuillez rentrer un nombre entier positif:\n");
//         scanf("%d",&x);
//     } while (x<0);
//     printf("x est positif\n");
//     printf("la racine de x est:\n %f\n",sqrt(x));
// }

/*exo 46*/

// int main(){
//     printf("entrez deux nombres: ");
//     int x,y;
//     scanf("%d %d",&x,&y);
//     printf("la somme de %d et %d donne %d\n",x,y,x+y);
//     printf("la difference de %d et %d donne %d\n",x,y,x-y);
// }

/*exo 47*/

// int main(){
//     printf("entrez un nombre: ");
//     int x;
//     scanf("%d",&x);
//     if (x%2==0){
//         printf("%d est pair\n",x);
//     }
//     else{
//         printf("%d est impair\n",x);
//     }
// }

/*exo 48*/

// int main(){
//     printf("entrez 3 nombres: ");
//     int x,y,z;
//     scanf("%d %d %d",&x,&y,&z);
//     if ((x<y)&&(x<z)){
//         printf("%d x est le nombre le plus petit",x);
//     }
//     else if ((y<x)&&(y<z)){
//         printf("%d y est le nombre le plus petit",y);
//     }
//     else{
//         printf("%d z est le nombre le plus petit",z);
//     }
// }

/*exo 50*/

// int main(){
//     printf("entrez 2 nombres a permuter: ");
//     int x,y,tmp;
//     scanf("%d %d",&x,&y);
//     printf("x vaut %d et y vaut %d\n",x,y);
//     tmp=x;
//     x=y;
//     y=tmp;
//     printf("x vaut mtn %d et y vaut %d\n",x,y);
// }

/*exo 51*/

// int main(){
//     int hd,md,sd,ht,mt,st;
//     printf("entrez l'heure de départ du train en hms\n");
//     scanf("%d %d %d",&hd,&md,&sd);
//     printf("entrez le temps de trajet du train en hms\n");
//     scanf("%d %d %d",&ht,&mt,&st);
//     int ah,am,as,aj;
//     ah=0;am=0;as=0;
//     if (sd+st>=60){
//         as=(sd+st)%60;
//         am=1;
//     }
//     else as=sd+st;
//     if (md+mt>=60){
//         am+=(md+mt)%60;
//         ah=1;
//     }
//     else am+=md+mt;
//     if (ah+=hd+ht>24){
//         ah+=(hd+ht)%24;
//         aj=1;
//     }
//     else ah+=hd+ht;
//     printf("l'heure d'arrivée prévue est:\n%dj:%dh:%dm:%ds\n",aj,ah,am,as);
// }

/*exo 53*/

// int main(){
//     printf("boucle for:\n");
//     int i,x,sum=0;
//     for (i=0;i<5;i++){
//         scanf("%d",&x);
//         sum+=x;
//     }
//     printf("%d\n",sum);
//     printf("boucle while:\n");
//     int i=0,x,sum=0;
//     while (i<5){
//         scanf("%d",&x);
//         sum+=x;
//         i++;
//     }
//     printf("%d\n",sum);
//     printf("boucle do while:\n");
//     int i=0,x,sum=0;
//     do{
//         scanf("%d",&x);
//         sum+=x;
//         i++;
//     } while (i<5);
//     printf("%d\n",sum);
// }

/*exo 57*/

// int main(){
//     int x,n,i,tmp;
//     printf("entrer un nombre x qui sera ajouté n fois a lui même:\n");
//     scanf("%d %d",&x,&n);
//     tmp=x;
//     for (i=1;i<n;i++){
//             tmp+=x;
//     }
//     printf("le résultat est: %d\n",tmp);
// }

/*exo 58*/

// int main(){
//     int n,i,j;
//     printf("entrer un nombre n qui sera le nombre de ligne du triangle étoilé:\n");
//     scanf("%d",&n);
//     for (i=0;i<=n;i++){
//         for (j=0;j<i;j++){
//             printf("*");
//         }
//         printf("\n");
//     }
// }

/*exo 61*/

// int main(){
//     int i,u1=0,u2=1,u,n,tmp;
//     printf("entrer un nombre n>2\n");
//     scanf("%d",&n);
//     printf("%d\n%d\n",u1,u2);
//     for (i=0;i<n;i++){
//         u=u2+u1;
//         u1=u2;
//         u2=u;
//         printf("%d\n",u);
//     }
// }

/*exo 63*/

// int main(){
//     int i,j;
//     for (i=1;i<=10;i++){
//         for(j=1;j<=10;j++){
//             printf("|%d*%d=%d|\n",i,j,i*j);
//         }
//         printf("_____________\n");
//     }
// }

/*exo 68*/

// int main(){
//     int x;
//     do{
//         printf("entrez un nombre positif: ");
//         scanf("%d",&x);
//     } while (x<0);
//     printf("%d\n",x);
// }

/*exo 96*/

// int main(){
// 	const int N = 10;
// 	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
// 	int B[] = {0, 2, 1, 3, 5, 4, 6, 8, 7, 9};

// 	int count = 0;
// 	for (int i = 0; i < N; i++)
// 		if (A[i] == B[i])
// 			count++;

// 	printf("%d\n", count);
// }

/*exo 97*/

// int main(){
//     const int N=5;
//     int A[] ={5,2,48,72,36};

//     int ind=0;
//     int pg=A[0];
//     for (int i=0; i<N;i++){
//         if (pg<A[i]){
//             pg=A[i];
//             ind=i;
//         }
//     }
//     printf("le plus grand nombre du tableau est %d d'indice %d",pg,ind);
// }

/*exo 98 marche pas*/

// int main(){
//     int N,tmp;
//     int i=0, j=0;
//     printf("entrez un nombre: ");
//     scanf("%d",&N);
//     for (i;i<N;i++){
//         printf("entrez un %dème nombre :",i);
//         scanf("%d",&tmp);
//         N[i]=tmp;
//     }
//     for (int i = 0; i < N; i++)
// 		printf("%d\n", N[i]);
//     printf("\n");
// }

