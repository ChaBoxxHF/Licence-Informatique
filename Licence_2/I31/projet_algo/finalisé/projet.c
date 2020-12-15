#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <gmp.h>

int main (){
    int n;
    unsigned long seed;
    mpz_t a ,b ,A ,B ,Ka ,Kb, p ,g;
    gmp_randstate_t r;
    mpz_inits ( a ,b ,A ,B ,Ka ,Kb ,p ,g ,NULL);
    seed = time (NULL);
    gmp_randinit_default (r);  /*initialise un état par défaut*/
    gmp_randseed_ui (r ,seed);
    gmp_printf("Valeur de n (bit): ");
    gmp_scanf("%d", &n);


    //generation d’un nombre premier de n bits
    do
    {
        mpz_urandomb (p ,r ,n);  /*génère un nombre compris entre 0 et (2^n)-1*/
        mpz_setbit (p ,n-1);    /*"set bit index in rop"*/
        mpz_nextprime (p ,p);   /*Set rop to the next prime greater than op.*/
    } while (mpz_sizeinbase(p , 2) != n);
    gmp_printf("\nNombre premier p = %Zd\n", p);


    // Calcul de la racine primitive
    mpz_sqrt(g, p);
    gmp_printf("\nRacine primitive g = %Zd\n\n", g);

    // Codes des personnes présentes
    gmp_printf("Les prochains nombres demandés devront être inférieur à p !\n\n");
    gmp_printf("Nombre d'Alice: ");
    gmp_scanf("%Zd", &a);
    gmp_printf("Nombre de Bob: ");
    gmp_scanf("%Zd", &b);


    // generation de deux nombres aleatoires inferieurs à p
    mpz_urandomm ( a , r , p ) ;
    mpz_urandomm ( b , r , p ) ;
    

    // Calcul des clés avec exponentiation modulaire
    mpz_powm ( A , g , a , p ) ;    /*expo modulaire*/
    gmp_printf ( "Alice envoie %Zd à Bob\n\n" , A ) ;
    mpz_powm ( B , g , b , p ) ;
    gmp_printf ( "Bob envoie %Zd à Alice\n\n" , B ) ;
    mpz_powm ( Ka , B , a , p ) ;
    gmp_printf ( "Clé secrète d'Alice , Ka = %Zd\n\n" , Ka ) ;
    mpz_powm ( Kb , A , b , p ) ;
    gmp_printf ( "Clé secrète de Bob , Kb = %Zd\n\n" , Kb ) ;
    if (Ka == Kb);
        printf("Les clés sont identiques\n");
}