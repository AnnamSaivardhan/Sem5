#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int z=0;
void* func(void* args){
    int z= 10;
    while(z>0){
        sleep(1);
printf("hi %d\n",z);
z--;}

}
void* func2(void* args){
    printf("hello\n");
}

int main(){
    pthread_t id;
    pthread_create(&id,NULL,func,NULL);
    sleep(8);
    pthread_create(&id,NULL,func2,NULL);
    pthread_join(id,NULL);
}