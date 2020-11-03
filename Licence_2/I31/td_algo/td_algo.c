#include <stdio.h>
#include <math.h>

int main()
{
    /*exo 44*/

    /*int x;
    do {
        printf("Veuillez rentrer un nombre entier positif:\n");
        scanf("%d",&x);
    } while (x<0);
    printf("x est positif\n");
    printf("la racine de x est:\n %f\n",sqrt(x));*/

    /*exo46*/

    /*int x,y;

    printf("entrez un entier pour x et pour y:\n");
    scanf("%d",&x);
    scanf("%d",&y);
    printf("la somme de x et y est:%d\n",x+y);
    printf("la différence de x et y est:%d\n",x-y);*/

    /*exo 47*/
    
    /*int x;
    printf("entrez un entier\n");
    scanf("%d",&x);
    if ((x%2)==0) printf("l'entier est paire");
    else printf("l'entier est impair\n");*/

    /*exo 48*/

    /*int x,y,z;
    printf("entrez 3 nombre x,y,z\n");
    scanf("%d %d %d",&x,&y,&z);
    if ((x<y)&&(x<z)) printf("x est le plus petit élément\n%d",x);
    else if ((y<x)&&(y<z)) printf("y est le plus petit élément\n%d",y);
    else printf("z est le plus petit élément\n%d",z);*/

    /*exo 49*/

     /*int a,b,c,d;
     printf("entrez 3 nombres a,b,c");
     scanf("%d %d %d",&a,&b,&c);
    printf("delta=b²-4ac, donc d:\n%d",d=((b*b)-(4*a*c)));
    if (d>0){
        printf("les deux solutions sont les suivantes:\n x1=%f",((-b-sqrt(d))/2*a));
        printf("x2=%f\n",((-b+sqrt(d))/2*a));
    }
    else if (d==0) printf("le résultat est unique et vaut -b/2a:\n%f\n",(-b/2*a));
    else printf("d est négatif donc il n'y a pas de résultat dans R\n");*/

    /*exo 50*/

    /*int x,y,tmp;
    printf("entrer les nombres a permuter:\n");
    scanf("%d %d",&x,&y);
    tmp=x;x=y;y=tmp;
    printf("les valeurs de x et y ont été échangés:\nx= %d y= %d\n",x,y);*/

    /*exo 51*/

    /*int hd,md,sd,ht,mt,st;
    printf("entrez l'heure de départ du train en hms\n");
    scanf("%d %d %d",&hd,&md,&sd);
    printf("entrez le temps de trajet du train en hms\n");
    scanf("%d %d %d",&ht,&mt,&st);
    int ah,am,as,aj;
    ah=0;am=0;as=0;
    if (sd+st>=60){
        as=(sd+st)%60;
        am=1;
    }
    else as=sd+st;
    if (md+mt>=60){
        am+=(md+mt)%60;
        ah=1;
    }
    else am+=md+mt;
    if (ah+=hd+ht>24){
        ah+=(hd+ht)%24;
        aj=1;
    }
    else ah+=hd+ht;
    printf("l'heure d'arrivée prévue est:\n%dj:%dh:%dm:%ds\n",aj,ah,am,as);*/

    /*exo 52*/

    /*int a,b;
    char op;
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
    }*/

    /*exo 53*/

    /*int x=0, y=0,z;
    while (y<10)
        ++y;
        x+=y;
    printf("A:x=%d; y=%d\n",x,y);
    x=y=0;
    while (y<10)
        x+= ++y;
    printf("B:x=%d; y=%d\n",x,y);
    y=1;
    while (y<10){
        x=y++;
        z=y++;
    }
    printf("C:x=%d; y=%d\n",x,y);
    for (y=1;y<10;y++) x=y;
    printf("D:x=%d; y=%d\n",x,y);
    for (y=1;(x=y)<10;y++);
    printf("E:x=%d; y=%d\n",x,y);
    for (x=0, y=1000;y>1;x++,y/=10);
    printf("F:x=%d; y=%d\n",x,y);*/

    /*exo 54*/

    /*int a,i=1,s=0;
    printf("version for\n");
    printf("rentrer 5 nombre:\n");
    for (i=0;i<5;i++) {
        scanf("%d",&a);
        s+=a;
    }
    printf("la somme des 5 nombre est :%d\n",s);*/
    /*printf("version while\n");
    printf("rentrer 5 nombre:\n");
    while (i<=5){
        scanf("%d",&a);
        s+=a;
        i++;
    }
    printf("la somme des 5 nombre est :%d\n",s);*/
    /*printf("version do...while\n");
    printf("rentrer 5 nombre:\n");
    do{
        scanf("%d",&a);
        s+=a;
        i++;
    } while(i<=5);
    printf("la somme des 5 nombre est :%d\n",s);*/

    /*exo 55*/

    /*int a,t=0,moy=0;
    printf("entrer une suite de nombre dont on va faire la moyenne\n la valeur ''-1'' stopera la saisie\n");
    do{
        scanf("%d",&a);
        if (a!=-1){
            moy+=a;
            t++;
        }
    } while (a!=-1);
    moy/=t;
    printf("La moyenne de votre saisie de taille %d est:\n%d\n",t,moy);*/

    /*exo 56*/

    /*int s=0,n,i;
    printf("entrer le nombre auquel la somme doit s'arrêter");
    scanf("%d",&n);
    for (i=0;i<=n;i++){
        s+=i;
    }
    printf("la somme des N premiers entiers est:\n%d\n",s);*/

    /*exo 57*/

    /*int x,n,i,tmp;
    printf("entrer un nombre x qui sera ajouté n fois a lui même:\n");
    scanf("%d %d",&x,&n);
    tmp=x;
    for (i=1;i<n;i++){
            tmp+=x;
    }
    printf("le résultat est: %d\n",tmp);*/

    /*exo 58*/

    /*int n,i,j;
    printf("entrer un nombre n qui sera le nombre de ligne du triangle étoilé:\n");
    scanf("%d",&n);
    for (i=0;i<=n;i++){
        for (j=0;j<i;j++){
            printf("*");
        }
        printf("\n");
    }*/

    /*exo 59*/

    /*int n,i,j;
    printf("entrer un nombre n:");
    scanf("%d",&n);
    for (i=0;i<=n;i++){
        for (j=0;j<pow(2,i);j++){
            printf("*");
        }
        printf("\n");
    }*/

    /*exo 60*/

    /*int n,i,j;
    printf("entrer un nombre n:");
    scanf("%d",&n);
    for (i=0;i<=n+1;i++){
        for (j=0;j<i*2;j++){
            printf("*");
        }
        printf("\n");
    }*/

    /*exo 61*/

    /*int i,u1=0,u2=1,u,n,tmp;
    printf("entrer un nombre n>2\n");
    scanf("%d",&n);
    printf("%d\n%d\n",u1,u2);
    for (i=0;i<n;i++){
        u=u2+u1;
        u1=u2;
        u2=u;
        printf("%d\n",u);
    }*/

    /*exo 62*/

    /*int a,i;
    printf("entrer un nombre >2\n");
    scanf("%d",&a);
    for (i=2;i<a;i++){
        if ((a%i)==0){
            printf("%d n'est pas premier car divible par %d\n",a,i);
            break;
        }
    }
    printf("%d est premier\n",a);*/

    /*exo 63*/

    /*int i,j;
    for (i=1;i<=10;i++){
        for(j=1;j<=10;j++){
            printf("|%d*%d=%d|\n",i,j,i*j);
        }
        printf("_____________\n");
    }*/

    /*exo 64*/

    /*int a,i,cpt=0;
    printf("entrez 10 nombres réels\n");
    for (i=0;i<10;i++){
        scanf("%d",&a);
        if (a<0){
            cpt+=1;
        }
    }
    printf("il y a %d nombres négatifs\n",cpt);*/

    /*exo 65*/

    /*int a,i;
    do{
        scanf("%d",&a);
    } while (a>0);*/

    /*exo 66*/

    /*int a=1,b=1,i;
    printf("entrez un suite de nombres a multiplier entre eux\n le 0 sera la condition d'arrêt\n");
    do{
        b*=a;
        scanf("%d",&a);
    } while (a!=0);
    printf("%d\n",b);*/

    /*exo 67*/

    /*nique*/

    /*exo 68*/

    /*int nbm=1702,pin;
    printf("entrer un code pin a 4 chiffre\n");
    do{
        scanf("%d",&pin);
        if(pin!=nbm) printf("code incorecte entrez un nouveau code pin\n");
    } while (pin!=nbm);
    printf("code correct\n");*/
}