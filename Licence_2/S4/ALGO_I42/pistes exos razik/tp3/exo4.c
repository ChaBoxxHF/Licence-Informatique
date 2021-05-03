/* ftok1.c */
#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
 
int main(int argc, char * argv[])
{
  printf("ftok1\n");
  printf("  Ma cle A: %d \n",ftok("ftok1.c",'A'));
  printf("  Ma cle B: %d \n",ftok("ftok1.c",'B'));
  return 1;
}

/* ftok2.c */
#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
 
int main(int argc, char * argv[])
{
  printf("ftok2\n");
  printf("  Ma cle A: %3d \n",ftok("ftok2.c",'A'));
  printf("  Ma cle B: %3d \n",ftok("ftok2.c",'B'));
  return 1;
}

/* ftok3.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
 
int main(int argc, char * argv[])
{
  printf("ftok3\n");
  printf("  Ma cle A: %d \n",ftok(getenv("HOME"),'A'));
  printf("  Ma cle B: %d \n",ftok(getenv("HOME"),'B'));
  return 1;
}