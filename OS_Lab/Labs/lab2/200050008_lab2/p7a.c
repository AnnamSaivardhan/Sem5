#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  
    
    int n;
    int z=n;
    int y=getpid();
    scanf("%d",&n);
    
    printf("Parent is:%d\n",getpid());

    printf("Number of children:%d\n",n);
    int x =fork();
    n--;
    if(!x) printf("Child %d is created\n",getpid());
    while(n && !x){
       
            x=fork();
            if(!x) printf("Child %d is created\n",getpid());
            if(x!=0){
                
                break;
            }
        
        n--;
    }
    wait(NULL);
    if(y==getpid()){
        printf("Parent exited\n");
    }else{
    printf("Child %d with parent %d exited\n",getpid(),getppid());
    }
    
    
    return 0;
}