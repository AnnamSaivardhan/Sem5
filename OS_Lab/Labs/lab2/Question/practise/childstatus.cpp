#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

//To know the stats of child use pid_t x = waitpid(child_pid, &integer_a,WNOHANG)
//if x is zero then the child is still running 
int main(){
    int f=fork();
    if(f==0){
        int t=8;
        while(t){
            printf("I am Child\n");
            sleep(1);
            t--;
        }
        printf("Child exiting\n");
    }else{
        printf("parent sleeping for 3 seconds\n");
        sleep(3);
        printf("parent Wokeup\n");
        while(1){
            int status;
            pid_t stat= waitpid(f,&status,WNOHANG);
            if(stat!=0){
                printf("Parent: Child terminated\n");
                break;
            }

            
        }
        printf("parent exiting\n");
    }
}