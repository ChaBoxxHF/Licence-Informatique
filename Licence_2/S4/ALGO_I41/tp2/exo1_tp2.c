#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

uint Increment(uint * A, unsigned char n, unsigned char b){
    int modif=0;
    int i=n;
    while((i>0)&&(A[i]==b-1)){
        A[i]=0;
        i-=1;
        modif+=1;
    }
    if (i<n){
        A[i]=A[i]+1;
        modif+=1;
    }
    return modif;
}

int main(){
    unsigned char n = 3;
    unsigned char b = 10;
    uint A[3]= {9,9,9};

    uint i = Increment(A,n,b);

    printf("%i\n",i);
}