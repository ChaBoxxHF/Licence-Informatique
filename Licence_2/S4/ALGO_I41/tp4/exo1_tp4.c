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
    float x;
    scanf("%f",&x);
    uint n;
    scanf("%d",&n);
    printf("%f puissance %d vaut: %f\n", x, n, Power(x,n));
}