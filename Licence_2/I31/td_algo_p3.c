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


int main()
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
}

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