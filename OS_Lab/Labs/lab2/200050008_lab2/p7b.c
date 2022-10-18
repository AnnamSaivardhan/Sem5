#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  
    
    int n;
   
    int y=getpid();
    scanf("%d",&n);
     int z=n;
    int arr[n];
    printf("Parent is:%d\n",getpid());

    printf("Number of children:%d\n",n);
    for(int i=0;i<n;i++){
        arr[i]=fork();
        if(arr[i]!=0) printf("Child %d is created\n",arr[i]);
        if(arr[i]==0){
            sleep(1);
            break;
        }
    }
    
    
    if(y==getpid()){
        z--;
        while(z){
         
            wait(NULL);
            z--;
        }
        printf("Parent exited\n");
    }else{
    printf("Child %d with parent %d exited\n",getpid(),getppid());
    }
    
    
    return 0;
}