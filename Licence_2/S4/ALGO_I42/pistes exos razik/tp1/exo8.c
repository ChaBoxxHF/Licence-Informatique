#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
 
 
int main(int argc, char *argv[])
{
 
  pid_t pid;
  int i;
 
  for (i = 1; i < argc; i++)
    {
     pid = fork();
     if (pid == 0) {
         execlp(argv[i], argv[i], NULL);
        /* si exec echoue il faut sortir du fils */
        /* sinon ce dernier va continuer a executer */
        /* la boucle for */
         printf("Erreur d'execution\n");
         exit(1);
        }
     else wait(0);
    }
  exit(0);
}