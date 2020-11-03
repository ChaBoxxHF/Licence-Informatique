#include <stdio.h>

/*exo 98-99*/

/*int main()
{
	const int N = 5;
	int nombres[N];
	int tmp;

	printf("Entrer un 1er nombre: ");
	scanf("%d", &nombres[0]);
	for (int i = 1; i < N; i++)
	{
		printf("Entrer un %dème nombre: ", i);
		scanf("%d", &tmp);

		if (nombres[i - 1] > tmp)
		{
			nombres[i] = nombres[i - 1];
			nombres[i - 1] = tmp;
			continue;
		}
		nombres[i] = tmp;
	}

	for (int i = 0; i < N; i++)
		printf("%d\n", nombres[i]);
}*/

/*exo 99 corrigé*/

/*int main(){
    const int N = 5;
    int nombres[N];
    for (int i = 0; i < N; i++){
        printf("Entrer un nombre: ");
    scanf("%d", &nombres[i]);
    }
    for (int i = N-1; i >=0; i--)
        printf("%d\n", nombres[i]);
}*/

/*exo 100*/

/*int main()
{
	const int N = 10;
	const int x = 5;
	int A[] = {0, 1, 5, 3, 4, 5, 6, 7, 8, 5};

	for (int i = 0; i < N; i++)
		if (A[i] == x)
			printf("A[%d] = %d\n", i, x);
}*/

/*exo 101*/


/*int main()
{
	int N = 10, x = 5;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

	int isFind = 0;
	for (int i = 0; i < N; i++)
		if (isFind || A[i] == x)
		{
			isFind = 1;
			A[i] = A[i + 1];
		}
	if (isFind)
		N--;

	for (int i = 0; i < N; i++)
		printf("%d\n", A[i]);
}*/

/*exo 101 corrigé*/


/*#define N 10
int main(){
    int A[N]={2,4,1,9,9,5,6,7,1,6};
    int i, x, j;
    int c=0;
    printf("Entrer x: ");
    scanf("%d", &x);
    for(i=0;i<N;i++){
    if(A[i]==x){
        c++;
        for(j=i;j<N-1;j++)
            A[j]=A[j+1];
            i--;
    }
    }
    for (i = 0; i < N-c; i++)
        printf("%d ", A[i]);
        printf("\n");
}*/


/*exo 102*/

/*int main(){
    int N = 10, x = 5;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    int x;
    int i=0;
    printf("entrez un nombre entre 0 et 9\n");
    scanf("%d",&x);
    do{

    } while (!=x)
}*/

/*correction*/

/*#define N 5

int main(){
	int A[N]={2,3,4,5,6};
	int g=0,d=N-1, m=(g+d)/2;
	int x,i;
	printf("saisir nb:");
	scanf("%d",&x);
	while (x!=A[m] && d-g>=0){
		if (x>A[m]){
			g=m+1;
			m=(g+d)/2;
		}
		else{
			d=m-1;
			m=(d+g)/2;
		}
	}
	if (x==A[m]){
		printf("%d  est à la position %d\n",x,m);
	}
	else{
		printf("%d n'est pas dans le tableau\n",x);
	}
}*/

/*exo 103*/

/*solution 1*/

/*#include <stdio.h>

#define N 10

int main()
{
  int vecteurs[2][N] = {{-1, 2, 3, 5, 2, 8, -3, 9, 7, 6},
                        {2, 3, 8, 9, 7, 1, -4, -5, 6, 9}};

  int prod_scal = 0;
  for (int i = 0; i < N; i++)
    prod_scal += vecteurs[0][i] * vecteurs[1][i];

  printf("%d\n", prod_scal);
}*/

/*SOLUTION 2*/

/*#include <stdio.h>

#define N 10

int main()
{
  int A[N] = {-1, 2, 3, 5, 2, 8, -3, 9, 7, 6};
  int B[N] = {2, 3, 8, 9, 7, 1, -4, -5, 6, 9};

  int prod_scal = 0;
  for (int i = 0; i < N; i++)
    prod_scal += A[i] * B[i];

  printf("%d\n", prod_scal);
}*/

/*exo 104*/

