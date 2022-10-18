#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include<sys/wait.h>
#include<stdlib.h>


/* 
----------------------------------------PIPE---------------------------------
+
*/


int main(){
    int fd[2];
    pipe(fd);
    //fd[1] is writing end and fd[0] is reading end
    int x=fork();

    
    if(x==0){
        //process B
        int fd2[2];
        pipe(fd2);
        int hh=fork();

            //process A
            if(hh==0){
                int inp1;
                scanf("%d",&inp1);
                printf("Process A input is: %d\n",inp1);
                close(fd2[0]);
                write(fd2[1],&inp1,sizeof(int));
                close(fd2[1]);
                exit(1);
            }
        
        wait(NULL);
        close(fd2[1]);
        int inp2; scanf("%d",&inp2);
        printf("Process B input is: %d\n",x);
        int from_A;
        read(fd2[0],&from_A,sizeof(int)); //printf("i got %d\n",from_A);
        close(fd2[0]);
        int res=from_A+x;
        write(fd[1],&res,sizeof(int));
        close(fd[1]);
        exit(0);
    } else{

        //process C
        wait(NULL);
        close(fd[1]);
        int fin;
        read(fd[0],&fin,sizeof(int));
        printf("Sum is %d\n",fin);
        close(fd[0]);
        

    }
}