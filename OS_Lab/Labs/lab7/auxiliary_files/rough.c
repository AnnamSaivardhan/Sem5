#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int z=0;
void* func(void* args){
printf("hi\n");
}
void* func2(void* args){
    printf("hello\n");
}

int main(){
    pthread_t id;
    pthread_create(&id,NULL,func,NULL);
    pthread_join(id,NULL);
    pthread_create(&id,NULL,func2,NULL);
    pthread_join(id,NULL);
}