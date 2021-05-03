#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
 
int pid, ppid, cpt;
 
void traitersignal(int sig)
  {
     cpt = 1;
  }
 
int main(int argc, char *argv[])
 
{
  pid = fork();
  if (pid == 0)
    {
      signal(SIGUSR1, traitersignal); 
      ppid = getppid();
      while (cpt <= 10) 
         {
           sleep(1);
          // printf("%d\n", cpt);
           cpt ++;
         }  
      kill(ppid, 3);
    }
  else
    {
      printf("Num fils : %d\n", pid);
      while(1);
    }  
  exit(0);  
}
