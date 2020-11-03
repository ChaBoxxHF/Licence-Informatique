#include <stdio.h>
#define print(int) printf("%d\n",int)
#define print3(x,y,z)\
printf("x=%d\ty=%d\tz=%d",x,y,z)
#define TYPE int

int main()
{
    /*exo1*/

    /*printf("Hellow world \n");*/

    /*exo2.1*/

    /*int x,y,z;
    x=2;y=1;z=0;
    x=x&&y||z;print(x);
    print(x||!y&&z);

    x=y=1;
    z=x++ -1;print(x);print(z);
    z+= -x ++ + ++y; print(x);print(z);
    z=x/++x;print(z);*/

    /*exo2.2*/

    /*int x;
    x=-3+4*5-6; print(x);
    x=3+4%5-6; print(x);
    x=-3*4%-6/5; print(x);
    x=(7+6)%5/2; print(x);*/

    /*exo2.3*/

    /*int x=2,y,z;
    x*=3+2;print(x);
    x*=y=z=4;print(x);
    x=y==z;print(x);
    x==(y=z);print(x);*/

    /*exo2.4*/

    /*int x=1,y=1,z=1;
    x+=y+=z;
    print(x<y?y:x);
    print(x<y?x++:y++);
    print(x);print(y);
    print(z+=x<y?x++:y++);
    print(y);print(z);
    x=3;y=z=4;
    print((z>=y>=x)?1:0);
    print(z>=y&&y>=x);*/

    /*exo2.5*/

    /*int x,y,z;
    x=03;y=02;z=01;
    print(x|y&z);
    print(x|y&~z);
    print(x^y&~z);
    print(x&y&&z);
    x=1;y=-1;
    print(!x|x);
    print(~x|x);
    print(x^x);
    x<<=3;print(x);
    y<<=3;print(y);
    y>>=3;print(y);*/

    /*exo2.6*/

    /*int x,y,z;
    x=y=z=1;
    ++x||++y&&++z;print3(x,y,z);

    x=y=z=1;
    ++x&&++y||++z;print3(x,y,z);

    x=y=z=1;
    ++x&&++y&&++z;print3(x,y,z);

    x=y=z=-1;
    ++x&&++y||++z;print3(x,y,z);

    x=y=z=-1;
    ++x||++y&&++z;print3(x,y,z);

    x=y=z=-1
    ++x&&++y&&++z;print3(x,y,z);*/

    /*rip exo 25/26*/

    /*exo 3.1*/

    /*char ch;
    int x;
    printf("entrez un caractère\n");
    x=getchar("%c\n",&ch);
    print(x);*/

    /*exo 3.2*/

    /*char ch;
    printf("entrez un caractère");
    scanf("%c",&ch);
    printf("Code ASCII de %c:%d\n",ch,ch);
    printf("on a fait l'exo 2");*/

    /*exo 4*/

    /*int x,y,m;
    if (x>=y) printf("%d\n",m=x);
    else printf("%d\n",m=y);*/

    /*int x,y,m;
    printf("entrez un nombre");
    scanf("%d\n",&x);
    printf("entrez un second nombre");
    scanf("%d\n",&y);
    m=x-y;
    if (m>=0) m=x;
    else m=y;
    print(m);*/

    /*exo 5*/

    /*int cdate,m,j;
    printf("entrez une date aaaammjj");
    scanf("%d\n",&cdate);
    int jour= cdate%100;
    int mois= cdate/100%100;
    int annee= cdate/10000;

    printf("Année:%d\nMois:%d\nJour:%d\n",annee,mois,jour);*/

    /*exo 7*/
    

}
/*exo 6*/
void fonction(TYPE n)
{
    TYPE i;
    int j,taille;
    taille=8*sizeof(TYPE);
    for(j=0;j<taille;j++)
    {
        i=1<<(taille -j -1); /*attention a la prio*/
        if (n&i) printf("1");
        else printf("0");
    }
    printf("\n");
}