#include <stdio.h>
#include <math.h>

int main(){
  int x;
    do {
        printf("Veuillez rentrer un nombre entier positif:\n");
        scanf("%d",&x);
    } while (x<0);
    printf("x est positif\n");
    printf("la racine de x est:\n %f\n",sqrt(x));
}
