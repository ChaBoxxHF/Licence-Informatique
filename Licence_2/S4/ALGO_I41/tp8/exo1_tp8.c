#include <stdio.h>
#include <stdlib.h>

typedef struct {
  uint n;        // longueur de la liste
  int *valeurs;
} tliste;

void Echanger(int *T, uint a, uint b)
{
    int tmp = T[a];
    T[a] = T[b];
    T[b] = tmp;
}

uint Partitionner(t_liste L, uint p, uint r)
{
    int i, j, x;
    x = L[p];
    i = p;
    j = r;
    while (L[j] > x)
        j--;
    while (i < j)
    {
        Echanger(L, i, j);
        do
        {
            j--;
        } while (L[j] >= x)
        do
        {
            i++;
        } while (L[i] <= x)
    }
    return j;
}

void TriRapide(tliste L, uint p, uint r)
{
    int q;

    if (p < r)
    {
        q = Partitionner(L, p, r);
        TriRapide(L, p, q);
        TriRapide(L, q+1, r);
    }
}

int main(int argc,char **argv){

}