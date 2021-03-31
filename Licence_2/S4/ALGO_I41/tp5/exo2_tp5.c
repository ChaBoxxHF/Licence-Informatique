#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long int ullong;
typedef unsigned char uchar;

uint *S2L(char *chaine){
    int a=strlen(chaine);
    int *tableau=malloc(a*sizeof(int));
    for (int i=0;i<a;i++){
        tableau[a-1-i]=chaine[i]- '0';
    }
    return tableau;
}

char *L2S(uint *liste) {
    int size = sizeof(liste) - 2;
    char *reverse = malloc(size * sizeof(char));
    uint i = 0;
    while (i < size) {
        reverse[size - i - 1] = liste[i] + '0';
        i++;
    }
    return reverse;
}

int main() {
    uint *inverse = S2L("320154");
    for(int i = 0; i < 6; i++)
        printf("%d\n", inverse[i]);

    char *reverse = L2S(inverse);
    printf("%s\n", reverse);
}