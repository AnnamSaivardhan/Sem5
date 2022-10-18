#include <stdio.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
int s=0;
void handler(int num){

   
}

int main(){
    int x=fork();

    struct sigaction action;
    action.sa_handler=handler;
    sigemptyset(&action.sa_mask);
    action.sa_flags=0;
    sigaction(SIGINT,&action.sa_mask,NULL);
    sigaction(SIGCHLD,&action.sa_mask,NULL);
    while(1){
        printf("%d\n",x);
        sleep(1);
    }
}


for(int i=0;tokens[i]!=NULL;i++){
				if(tokens[i]=="&&"){
					an=i+1;
					int z=fork();
					printf("%d\n",z);
					if(z==0){
					char* xx[i+1];
					for(int j=0;j<i;j++){
						xx[j]=tokens[j];
						printf("%s\n",xx[j]);
					}
					xx[i]=NULL;
					execvp(xx[0],xx);
					exit(0);
				}
				}
				if(tokens[i]=="&&"){
				wait(NULL);
				sleep(5);
				}
			}