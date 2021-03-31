#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long int ullong;
typedef unsigned char uchar;

ullong Factorielle(uchar n){
    ullong result=1;
    for (uchar i=1;i<=n;i++){
        result*=i;
    }
    return result;
}

int main(){
    printf("%llu\n",Factorielle(50));
}