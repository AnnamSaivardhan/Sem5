
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  
    
    auto pid=fork();
    if(pid!=0){
    printf("Parent : My process ID is:%d\n",getpid());
    printf("Parent : The child process ID is:%d\n",pid);
    sleep(60);
    }else{
    printf("Child : My process ID is:%d\n",getpid());
    printf("Child : The parent process ID is:%d\n",getppid());
    printf("Check child process state\n");
    printf("Press any key to continue\n");
    getchar();
    printf("Check child process state again\n");
    }

    
    
    return 0;
}