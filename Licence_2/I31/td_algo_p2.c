#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*#include <defs.h>
#define LOW 0
#define HIGH 5
#define CHANGE 2*/

/*exo 69*/

/*int f1(int i){return i+1;}

int f2(int i){return i++;}

int f3(int i){
    printf("f3:%d\n",i==0);
    return i;
}

int f4(int i){
    printf("f4:%d\n",i=0);
    return i;
}

int main(){
    int a,b;
    a=f1(0);
    b=f2(1);
    printf("1,a=%d, b=%d\n",a,b);
    a=f3(a);
    b=f4(a);
    printf("2:a=%d, b=%d\n",a,b);
}*/

/*exo 70*/

/*marche pas car la biblio defs.h existe pas
int i=LOW;

int workover(int i){
    i=(i%i)*((i*i)/(2*i)+4);
    PRINT1(d,i);
    return(i);
}

int reset(int i){
    i=i<=CHANGE?HIGH:LOW;
    return( i);
}

main(){
    auto int i=HIGH;
    reset(i/2); PRINT1(d,i);
    reset(i=i/2); PRINT1(d,i);
    i=reset(i/2); PRINT1(d,i);
    workover(i); PRINT1(d,i);
}*/

/*exo 74*/

int maxi(int x,int y){
    if (x==y) return 0;
    else if (x<y) return y;
    else return x;
}

/*int main(){
    printf("%d\n",maxi(8,8));
}*/

/*exo 75*/

int valabs(int x){
    if (x>=0) return x;
    else return -x;
}

/*int main(){
    printf("%d\n%d\n",valabs(-5),valabs(6));
}*/

/*exo 76*/

int lppd10(int x, int y){
    if (valabs(10-x)>valabs(y-10)) return y;
    else if (valabs(10-x)<valabs(y-10)) return x;
    else return maxi(x,y);
}

/*int main(){
    printf("%d\n%d\n%d\n",lppd10(5,8),lppd10(8,5),lppd10(0,20));
}*/

/*exo 78*/

int fact(int n){
    if (n<0){
        printf("error\n");
        exit(1);
    }
    else{
        int c=1,i;
        for (int i=1;i<=n;i++) c*=i;
        return c;
    }
}

/*int main(){
    printf("%d\n%d\n",fact(8),fact(0));
}*/

/*exo 79*/

/*int aleat(int x){
    int a;
    printf("entrer un valeur qui sera la limite de l'aléatoire");
    scanf("%d",&x);
    rand(x);
}*//*????*/

/*int main(){
    printf("%d\n",aleat(50));
}*/

/*exo 80*/

/*fack*/

/*exo 81*/

int sommeentiers(int n){
    int s=0;
    for (int i=0;i<=n;i++){
        s+=i;
    }
    return s;
}

/*int main(){
    int n;
    printf("entrer un nombre:");
    scanf("%d",&n);
    printf("somme des premiers entiers = %d\n",sommeentiers(n));
}*/

/*exo 82*/

int sommecarre(int n){
    int s=0;
    for (int i=0;i<=n;i++){
        s+=(i*i);
    }
    return s;
}

/*int main(){
    int n;
    printf("entrer un nombre:");
    scanf("%d",&n);
    printf("somme des premiers entiers = %d\n",sommecarre(n));
}*/

/*exo 83*/

int sommeproduit(int n){
    int s=0;
    for (int j=2;j<=n;j++){
        for (int i=2;i<=j;i++){
            s+=(i*j);
        }
    }
    return s;
}

/*int main(){
    int n;
    printf("entrer un nombre:");
    scanf("%d",&n);
    printf("somme des premiers entiers = %d\n",sommeproduit(n));
}*/

/*exo 84*/

int reste(int x,int y){

    int toSub = x, count = 0;
	while (toSub >= y)
	{
		toSub -= y;
		count++;
	}
	return toSub;
}

/*int main(){
    int x,y;
    printf("entrez un nombre pour x qui sera diviser par le nombre y");
    scanf("%d %d",&x,&y);
    printf("reste(%d, %d)=%d\n",x,y,reste(x,y));
}*/

/*exo 85*/

int estdivisiblepar(int x,int y){
    if (x%y==0) return 1;
    else return 0;
}

/*exo 86*/

int sommeDesImpairs(int n)
{
	int somme = 0;
	for (int i = 0; i < n; i++)
	{
		if (i % 2 == 1)
			somme += i;
	}
	return somme;
}

/*int main(){
    int n;
    printf("entrez un nombre");
    scanf("%d",&n);
    printf("%d\n",sommeDesImpairs(n));
}*/

/*exo 87*/

int puissance(int x, int n)
{
	if (n < 0)
	{
		printf("n ne peut pas être négatif!\n");
		exit(EXIT_FAILURE);
	}
	int p = 1;
	for (int i = 0; i < n; i++)
		p *= x;
	return p;
}

/*int main()
{
	int x, n;
	printf("Entrer un nombre x et sa puissance n: \n");
	printf("x=");
	scanf("%d", &x);
	printf("n=");
	scanf("%d", &n);
	printf("Puissance(%d, %d)=%d\n", x, n, puissance(x, n));
}*/

/*exo 88*/

int est_premier(int n)
{
	for (int i = 2; i < n; i++)
		if (n % i == 0)
			return 0;

	return 1;
}

void premiers_premier(int n)
{
	if (!est_premier(n))
		exit(EXIT_FAILURE);

	for (int i = 0; i < n; i++)
		if (est_premier(i))
			printf("%d est aussi un nombre premier\n", i);
}

/*int main()
{
	int n;
	printf("Entrer un entier n: ");
	scanf("%d", &n);

	if (est_premier(n))
		printf("%d est premieeeer\n", n);
	else
		printf("%d n'est pas premier\n", n);
	premiers_premier(n);
}*/

/*exo 89*/

int estDivisiblePar(int x, int y)
{
	return x % y == 0;
}

int estParfait(int x)
{
	int somme = 0;
	for (int i = 1; i < x; i++)
	{
		if (estDivisiblePar(x, i))
			somme += i;
	}
	return somme == x;
}

/*int main()
{
	int n, i = 1, count = 0;
	printf("Entrer un nombre n: ");
	scanf("%d", &n);

	while (count < n)
	{
		if (estParfait(i))
		{
			printf("%d est parfait.\n", i);
			count++;
		}
		i++;
	}
}*/

/*exo 90*/

int estdansrectangle(int x1,int y1,int x2,int y2,int x,int y){
    if ((x>x1) && (x<x2)){
        if ((y>y1) && (y<y2)) return 1;
        else return 0;
    }
    return 0;
}

int estdanscontour(int x1,int y1,int x2,int y2,int x,int y){
    if ((x==x1) || (x==x2)){
        if ((y==y1) || (y==y2)) return 1;
        else return 0;
    }
    return 0;
}

int estexterieur(int x1,int y1,int x2,int y2,int x,int y){
    if ((x<x1) || (x>x2)){
        if ((y<y1) || (y>y2)) return 1;
        else return 0;
    }
    return 0;
}

int estinterrieur (int x1,int y1,int x2,int y2,int x,int y){
    if ((x==x1) || (x==x2)){
        if ((y==y1) || (y==y2)) return 1;
        else return 0;
    }
    return 0;
}

/*int main(){
    int x1,y1,x2,y2,x,y;
    printf("entrez les valeurs de x1,x2,y1,y2\nx1=");
    scanf("%d",&x1);
    printf("x2=");
    scanf("%d",&x2);
    printf("y1=");
    scanf("%d",&y1);
    printf("y2=");
    scanf("%d",&y2);
    printf("choisissez les coordonées de P(x,y)");
    printf("x=");
    scanf("%d",&x);
    printf("y=");
    scanf("%d",&y);
    if (estdansrectangle(x1,y1,x2,y2,x,y)==1){
        printf("le point P (%d,%d) est dans le rectangle\n",x,y);
    }
    else printf("le point P (%d,%d) n'est pas dans le rectangle\n",x,y);
    if (estdanscontour(x1,y1,x2,y2,x,y)==1){
        printf("le point P (%d,%d) est sur le contour du rectangle\n",x,y);
    }
    else printf("le point P (%d,%d) n'est sur le contour du rectangle\n",x,y);
    if (estexterieur(x1,y1,x2,y2,x,y)==1){
        printf("le point P (%d,%d) est en dehors du rectangle\n",x,y);
    }
    else printf("le point P (%d,%d) n'est pas en dehors du rectangle\n",x,y);
    if (estinterrieur(x1,y1,x2,y2,x,y)==1){
        printf("le point P (%d,%d) est en a l'interrieur du rectangle\n",x,y);
    }
    else printf("le point P (%d,%d) n'est pas a l'interrieur du rectangle\n",x,y);
}*/

/*exo 91*/

int estdansunion(int x11,int y11,int x12,int y12,int x21,int y21,int x22,int y22,int x,int y){
    if ((x>x11 || x<x12)&&(x>x21 || x<x22)){
        if ((y>y11 || y<y12)&&(y>y21 || y<y22)) return 1;
        else return 0;
    }
    return 0;
}
/*skip*/

/*int main(){
    int x11,y11,x12,y12,x21,y21,x22,y22,x,y;
    printf("entrez les valeurs de x1,x2,y1,y2\nx11=");
    scanf("%d",&x11);
    printf("x12=");
    scanf("%d",&x12);
    printf("y11=");
    scanf("%d",&y11);
    printf("y12=");
    scanf("%d",&y12);
    printf("x21=");
    scanf("%d",&x21);
    printf("x22=");
    scanf("%d",&x22);
    printf("y21=");
    scanf("%d",&y21);
    printf("y22=");
    scanf("%d",&y22);
    printf("choisissez les coordonées de P(x,y)");
    printf("x=");
    scanf("%d",&x);
    printf("y=");
    scanf("%d",&y);
    if (estdansunion(x11,y11,x12,y12,x21,y21,x22,y22,x,y)==1) printf("P(%d,%d) est dans soit dans R1(%d,%d,%d,%d) soit dans R2(%d,%d,%d,%d) soit dans les 2\n",x,y,x11,y11,x12,y12,x21,y21,x22,y22);
    else printf("P(%d,%d) n'est dans aucun des deux rectangle",x,y);
}*/

/*exo 92*/

int seriegeometrique(int x,int n){
    int s=0;
    for (int i=0;i<=n;i++){
        s+=pow(x,i);
    }
    return s;
}

/*int main(){
    int x,n;
    printf("entrez une valeur pour x et n\n");
    scanf("%d %d",&x,&n);
    printf("le résulat de la seriegeometrique(%d,%d) est %d",x,n,seriegeometrique(x,n));
}*/

/*exo 93*/

int jumeaux(int a, int b)
{
	return est_premier(a) && est_premier(b) && (a == b + 2 || b == a + 2);
}

/*int main(){
    int a,b;
    printf("entrez un nombre entier premier pour a et b\na=");
    scanf("%d",&a);
    printf("b=");
    scanf("%d",&b);
    if (jumeaux(a,b)==1) printf("%d et %d sont jumeaux",a,b);
    else printf("%d et %d ne sont pas jumeaux",a,b);
}*/

/*exo 94*/

int nbDeChiffres(int x)
{
	int nbr = 0;
	while (x > 0)
	{
		x /= 10;
		nbr++;
	}
	return nbr;
}

int estPair(int x)
{
	return nbDeChiffres(x) % 2 == 0;
}

int extraitNombre(int x, int n, int lg)
{
	return (int)(x / pow(10, n)) % (int)pow(10, lg);
}

int sommeDesChiffres(int x)
{
	int somme = 0, m;
	while (x >= 10)
	{
		m = floor(x / 10);
		somme += x - 10 * m;
		x = m;
	}
	return x + somme;
}

/*int main(){
    int x = 45863047;
	printf("Entrer un nombre x: ");
	scanf("%d", &x);

	if (!estPair(x))
		exit(EXIT_FAILURE);

	int nC = nbDeChiffres(x);
	int eN_1 = extraitNombre(x, 0, floor(nC / 2));
	int eN_2 = extraitNombre(x, floor(nC / 2), nC);

	int estCouicable = sommeDesChiffres(eN_1) == sommeDesChiffres(eN_2);
	printf("%d est couicable ? : %s\n", x, estCouicable ? "Oui" : "Non");
}*/

/*exo 95*/

/*int main()
{
	char a[] = "un\ndeux\ntrois\n";
	char b[12] = "un deux trois";
	char c[] = 'abcdefg';
	char d[] = "Cette "
						 "phrase"
						 "est coupée";
	char e[2] = {'a', '\0'};
	char f[4] = {'a', 'b', 'c'};
	char g[4] = "'o'";
}*/

/*exo 96*/

/*int main()
{
	const int N = 10;
	int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int B[] = {0, 2, 1, 3, 5, 4, 6, 8, 7, 9};

	int count = 0;
	for (int i = 0; i < N; i++)
		if (A[i] == B[i])
			count++;

	printf("%d\n", count);
}*/

/*exo 97*/

/*int main()
{
	const int N = 8;
	int A[] = {0, -1, 8, 9, 18, 2, 3, 4};

	int max = A[0], max_i = 0;
	for (int i = 1; i < N; i++)
	{
		if (A[i] > max)
		{
			max = A[i];
			max_i = i;
		}
	}

	printf("A[%d] = %d est le plus grand élement.\n", max_i, max);
}*/
