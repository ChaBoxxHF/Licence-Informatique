#include <stdio.h>
#include <stdlib.h>


uint PairOuImpair(uint n){
    if (n%2==0){
        return n=n/2;
    }
    else{
        return n=n*3+1;
    }
}

uint syracuse(uint u0){
    int i=0;
    while (u0>1){
        PairOuImpair(n);
        printf("%d\n",PairOuImpair(n));
        i++;
    }
}

int main(){
    uint a= syracuse(3);
    printf("%d\n",a);
}