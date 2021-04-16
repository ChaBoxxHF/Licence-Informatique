#include <stdio.h>
#include <stdlib.h>

typedef struct {
  uint n;        // longueur de la liste
  int *valeurs;
} tliste;

void Copier(tliste X, uint i, tliste Y, uint j, uint n){
    
    int *tableau=malloc(((i+n-1)+(j+n-1))*sizeof(int));
    for (uint a=j;a<((i+n-1)+(j+n-1));a++){
        if (a<j+n-1)
            tableau[a]=Y[a];
        else if (a>j+n-1)
            tableau[a]=X[a];
    }
}

int main(int argc, char **argv){
    
}