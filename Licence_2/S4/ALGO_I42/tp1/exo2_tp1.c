#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(void) {
  int pid = fork();
  if (pid==0){
    pid_t ppid = getpid();
    printf("je suis le fils, mon père a pour PID: %d\n",getppid());
  }
  else{
      printf("je suis le père, mon fils a pour PID: %d\n",pid);
  }
  while(1);
}
