#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
 
int main(void)
{
 
 pid_t pid, ppid;
 
 ppid = getpid();
 pid = fork();
 if (pid > 0) printf("Je suis le pere, mon fils a pour PID: %d\n",pid);
   else printf("Je suis le fils, mon pere a pour PID: %d\n",ppid);
 return 0;
}