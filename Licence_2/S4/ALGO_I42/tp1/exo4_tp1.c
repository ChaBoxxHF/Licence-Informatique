#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

void traitersignal(int sig) {
   printf("Signal %d bien recu\n", sig);
}

int main(void) {
  pid_t pid= fork();
  if (pid==0){
    sleep(5);
    printf("envoie signal kill");
    kill(getppid(),SIGUSR1);
  }
  else{
    pause();
    signal(SIGUSR1, traitersignal);
  }
}
