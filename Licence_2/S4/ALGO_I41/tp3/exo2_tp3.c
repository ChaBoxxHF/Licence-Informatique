#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void exchange(int *liste,int i, int j){
    int tmp;
    tmp=liste[i];
    liste[i]=liste[j];
    liste[j]=tmp;
}

uint idIS(int *liste,int i,int n){
    int j;
    int a=liste[i];
    int imin=i;
    for (j=i;j<n;j++){
        if(a>liste[j]){
            a=liste[j];
            imin=j;
        }
    }
    return imin;
}

void TriSelection(int *liste, ushort n){
    int i=0,imin;
    while (i<n){
        imin=idIS(liste,i,n);
        exchange(liste,i,imin);
        i++;
    }
}

int main(){
    int liste[]={858,56558,685258,5558,7226,723};
    TriSelection(liste,6);
    int i;
    for (i=0;i<6;i++){
        printf("%d\n",liste[i]);
    }
}