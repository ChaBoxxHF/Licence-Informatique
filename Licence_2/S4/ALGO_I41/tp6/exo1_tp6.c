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

typedef unsigned long long ullong;

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

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

ullong TriSelection(int *T, uint n){
    ullong cpt=0;
    uint imin;
    for (int i=0;i<n;i++){
            imin= IdxMin(T,i,n);
            exchange(T,i,imin);
            cpt++;
    }
    return cpt;
}

ullong TriBulles(int *T, uint n){

    //cassé
    bool permut = true;
    ullong cpt=0;
    
    while (permut== true){
        permut = false;
        cpt ++;
        for (int i=0;i<n;i++){
            if (T[i]>T[i+1]){
                permut=true;
                exchange(T,i,i+1);
            }
        }
    }
    for (int i=0;i<n;i++){
        printf("%5d",T[i]);
    }
    return cpt;
}

// naze
//     uint i=0;
//     ullong cpt=0;
//     while (i<n){
//         uint j=i;
//         while (j<n){
//             cpt++;
//             if (T[j]<T[j+1]){
//                 exchange(T,j,j+1);
//             }
//             j++;
//         }
//         i++;
//     }
//     return cpt;
// }

ullong TriInsertion(int *T,uint n){

}

int main(int argc,char **argv){
    int T[5]={1,2,3,4,5};
    printf("%lld\n",TriBulles(T,10));
    return 0;
}