#include <stdio.h>
#include <pthread.h>

typedef struct
{
    int a;
    int b;
}my_type;


void* my_func(void* arg){
    my_type* var = (my_type*)arg;
    printf("a:%d   b:%d\n",var->a,var->b);
}


int main(){
    pthread_t p;
    my_type ag;
    ag.a = 1;
    ag.b = 2;
    pthread_create(&p,NULL,my_func,(void*) &ag);
    pthread_join(p,NULL);
}