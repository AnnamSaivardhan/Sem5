#include <stdio.h>
#include <pthread.h>

int balance=0;
lock_t 

void* my_func(void* arg){
    for(int i=0;i<10000;i++){
        balance+=1;
    }
}

int main(){
    pthread_t p1,p2;
    pthread_create(&p1,NULL,my_func,NULL);
    pthread_create(&p2,NULL,my_func,NULL);
    pthread_join(p1,NULL);
    pthread_join(p2,NULL);
    printf("%d\n",balance);
}
