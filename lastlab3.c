#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main()
{

int fd[2], i = 0;
pipe(fd);
pid_t pid = fork();

if(pid > 0) {
	wait(NULL);
	close(0);

	close(fd[1]);

	dup(fd[0]);
	int num,c;

	int n = read(fd[0], &num, sizeof(num));
	int i,flag = 0; 
	if (num == 0 || num == 1){
		flag = 1;}

	for (i = 2; i <= num / 2; ++i) {
   	 if (num % i == 0) {
     		 flag = 1;
     		 break;
   	 }
  	}

  if (flag == 0)
    printf("%d is a prime number.\n", num);
  else
    printf("%d is not a prime number.\n", num);

}
else if( pid == 0 ) {
	int num;
	printf("Enter a number: ");
	scanf("%d", &num);

	close(fd[0]);

	close(1);	

	dup(fd[1]);
	write(1, &num, sizeof(num));
	
}

else {
	perror("error\n"); //fork()
}
}
