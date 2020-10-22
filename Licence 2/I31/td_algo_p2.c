#include <stdio.h>
#include <stdlib.h>
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

int main(){
    int x,y;
    printf("entrez un nombre pour x qui sera diviser par le nombre y");
    scanf("%d %d",&x,&y);
    printf("reste(%d, %d)=%d\n",x,y,reste(x,y));
}

/*exo 85*/

int estdivisible par(int x,int y){
    if (x%y==0) return 1;
    else return 0;
}