#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main(void) {
    char name[20];
    pid_t pid = fork();
 
    if(pid == 0) {
      for(int i = 0; i < 4; i++) {
      	printf("Enter name: ");
      	fgets(name,20,stdin);
      	printf("Student Name : %s",name);
      	}
      	exit(0);
    	
    }
    else  {
      wait(NULL);
      printf("Job is done.\n");
    }
 
  return EXIT_SUCCESS;
}
