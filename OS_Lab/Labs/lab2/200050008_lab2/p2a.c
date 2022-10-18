#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>


int main(){
    int n;
    scanf("%d",&n);
    int pid=fork();
    char s;
    if(pid==0){
         s='C';
    }else{
         s='P';
    }
    
    int x= getpid();
    for(int i=0;i<n;i++){
        int r;
        if(s=='C'){
            r=i+1;
        }else{
            r=n+i+1;
        
        }
        printf("%c %d %d\n",s,x,r);
    }
}