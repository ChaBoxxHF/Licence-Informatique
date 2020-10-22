#include <stdio.h>

int main()
{
    int n=15, p=10, q=5, r=1;
    q = n < p ? n ++ : p ++;
    printf("\nC:n=%d,p=%d,q=%d,r=%d",n,p,q,r);
    q = n > p ? n ++ : p ++;
    printf("\nC:n=%d,p=%d,q=%d,r=%d",n,p,q,r);
}