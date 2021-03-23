#include <stdio.h>
#include <stdlib.h>

double Power(float x, uint n){
    double result=x;
    for (int i=1;i<n;i++){
        result*=x;
    }
    return result;
}

int main(){
    printf("entrez un x:");
    float x;
    scanf("%f",&x);
    printf("entrez un n:");
    uint n;
    scanf("%d",&n);
    printf("x=%f puissance n=%u vaut: %f\n", x, n, Power(x,n));
}