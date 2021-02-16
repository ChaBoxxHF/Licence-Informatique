#include <stdio.h>
#include <math.h>

int fact(int n){
    if (n<=0){
        printf("error\n");
        exit(1);
    }
    else{
        int c=1,i;
        for (i=1;i<=n;i++) c*=i;
        return c;
    }
}

int pgcd(int a, int b){

    int pgcd, i;
    for(i=1; i <= a && i <= b; ++i)
    {
        if(a%i==0 && b%i==0)
            pgcd = i;
    }
  
    return pgcd;
}

int ppcm(int a, int b){
    return a*b/pgcd(a,b);
}

int main()
{
    /*exo 1*/

    /*int a,b,c=1;
    char op;
    do{
        printf("entrer un calcul a faire dans le format suivant : a (opérateur) b\n");
        scanf("%d %c %d",&a,&op,&b);
        switch(op){
            case '+':
                printf("%d\n",a+b);
                break;
            case '-':
                printf("%d\n",a-b);
                break;
            case '*':
                printf("%d\n",a*b);
                break;
            case '/':
                printf("%d\n",a/b);
            case '%':
                printf("%d\n",a%b);}
        printf("voulez vous continuer?(1=oui 0=non): ");
        scanf("%d",&c);
    } while (c==1);*/

    /*exo 2*/

    /*int x,i=0;
    printf("entrez un nombre x: ");
    scanf("%d",&x);
    while (i*i<=x) {
        i++;}
    printf("Le plus petit carré supérieur a %d est %d\n",x,i*i);*/

    /*exo 3*/

    /*int n,q,cpt=0;
    printf("veuillez entrer un nombre: ");
    scanf("%d",&n);
    q=n;
    do{
        n/=10;
        cpt+=1;
    } while (n>0);
    printf("il y a %d chiffre dans %d\n",cpt,q);*/

    /*exo 4*/

    /*int x,i,s=0;
    printf("entrez un nombre différent de 0: ");
    scanf("%d",&x);
    if (x==0) printf("error: nombre=0 impossible\n");
    else{
        for (i=1;i<x;i++){
            s+=i*i;
        }
        printf("somme des carré=%d\n",s);
    }*/

    /*exo 5*/

    /*int x=0,s=0,m,i=-1,v,j=0;
    printf("entrez des nombres (-1 sera la condition d'arrêt):\n");
    do{
        s+=x;

        scanf("%d",&x);
        i++;
    } while (x!=-1);
    m=s/i;
    printf("la moyenne est: %d\nla variance est: %d\n",m,v);*/
    /*osef variance voir github axel*/
/*v+=(val(i)-moy)²  v=v/i */

    /*exo 6*/

    /*int n,x,i;
    printf("entrez un nombre :");
    scanf("%d",&n);
    i=n;
    printf("l'ordre des coefs de (x+1)^n est:");
    while (i>=0){
        printf("x^%d ",i);
        i--;
    }
    printf("\n");*/

    /*int x,y,n,s=0,i,r;
    printf("entrez 3 nombres :");
    scanf("%d %d %d",&x,&y,&n);
    i=n;
    do{
        r=((fact(n))/(fact(i)*fact(n-i)));
        i--;
        s+=r;
    } while (i>0);
    printf("le résultat de (x+y)^n est : %d\n",s);*/
    /*give up*/

    /*int a, b;
	printf("Entrer les nombre p et q:\n");
	printf("a=");
	scanf("%d", &a);
	printf("b=");
	scanf("%d", &b);

	printf("Pgcd(%d, %d)=%d\n", a, b, pgcd(a, b));
    printf("Ppcm(%d, %d)=%d\n", a, b, ppcm(a, b));*/

    /*exo 8*/

    /*printf("%d\n",fact(8));
    int a;
    printf("entrer un nombre");
    scanf("%d",&a);
    printf("la factorielle de a est: %d\n",fact(a));*/
}