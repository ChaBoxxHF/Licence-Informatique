/* Dans cet exercice on nous demande de créer des tableaux
aléatoirement et de les trier avec des tris empiriques
(tri selection, tri propagation, tri insertion) afin de
calculer leur complexité*/

/*pour faire des nombres random :

#include <time.h>
#include <stdlib.h>

srand(time(NULL));   // Initialization, should only be called once.
int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void exchange(int *liste,int i, int j){
    int tmp;
    tmp=liste[i];
    liste[i]=liste[j];
    liste[j]=tmp;
}

/*int* GenTabTri(uint n){
    int* tab=malloc(n*sizeof(int));
    for (int i=0;i<n;i++){
        tab[i]=i+1;
    }
    return tab;
}*/

int* GenPerm(uint n){
    int* tab=malloc(n*sizeof(int));
    for (int i=0;i<n;i++){
        tab[i]=i+1;
    }
    srand(time(NULL));
    int r;
    for (int j=0;j<n;j++){
        while (r<j){
            r= rand()%n;
        }
        exchange(tab,j,r);
    }
    return tab;
}

uint IdxMin(int *liste,int i,int n){
    int j;
    int a=liste[i];
    int imin=i;
    for (j=i;j<n;j++){
        if(a>liste[j]){
            a=liste[j];
            imin=j;
        }
    }
    return imin;
}

int main(int argc,char **argv){
    int n;
    printf("entrez un nombre :");
    scanf("%d",&n);
    int* tab=GenPerm(n);
    for (int i=0;i<n;i++){
        printf("%d ",tab[i]);
    }
    printf("\n");
}