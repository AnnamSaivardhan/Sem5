
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  
    
    auto pid=fork();
    if(pid!=0){
    printf("Parent : My process ID is:%d\n",getpid());
    printf("Parent : The child process ID is:%d\n",pid);
    }else{
    printf("Child : My process ID is:%d\n",getpid());
    printf("Child : The parent process ID is:%d\n",getppid());
    }

    if(pid==0){
        sleep(2);
        printf("\n");
        printf("Child : After sleeping for 5 seconds\n");
        printf("Child : My process ID is:%d\n",getpid());
        printf("Child : The parent process ID is:%d\n",getppid());
    }
    
    return 0;
}