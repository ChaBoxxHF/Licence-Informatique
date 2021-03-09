#include <stdio.h>
#include <stdlib.h>
#include <string.h>

uint PairOuImpair(uint n){
    if (n%2==0){
        printf("%d est pair",n);
        int n=n/2;
    }
    else{
        printf("%d est impair",n);
        int n=n*3+1;
    }
}

int main(){
    uint n;
    scanf("%d",&n);
    uint a= PairOuImpair;
    printf("%d",a);
}