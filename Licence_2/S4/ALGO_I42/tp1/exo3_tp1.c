#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(void) {
  int n=0;
  pid_t pid = fork();
  if (pid==0){
    printf("je suis le fils et j'incrémente n de 1\n");
    n++;
    printf("voici le résultat: %d\n",n);
  }
  else{
    printf("je suis le père et j'incrémente n de 1\n");
    n++;
    printf("voici le résultat: %d\n",n);
  }
  fflush(stdout);
  sleep(5);
  printf("voici le résultat final %d\n",n);
}
