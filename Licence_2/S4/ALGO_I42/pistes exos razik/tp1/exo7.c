#include <unistd.h>
#include <stdlib.h>
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
        }
     else wait(0);
    }
  exit(0);
}