#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int sum = 0;
int odd = 0;
int even = 0;
int min = INT_MAX;
int max = INT_MIN;


//CREATE A STRUCTRE TO STORE PRODUCER'S TASKS
typedef struct
{
    int tm;
    char type;
} my_arg;




int main(int argc, char *argv[])){

    if(argc !=3){
        printf("Usage: ./producer_consumer <file path> <number of consumers>\n");
        exit(1);
    }
    int num_consumers = atoi(argv[2]);
    pthread_t* consumers = (pthread_t*)malloc(num_consumers*sizeof(pthread_t));
    for(int i=0;i<num_consumers;i++){
        pthread_create(&consumers[i],NULL,consumer,NULL);
    }
    FILE* fp = fopen(argv[1],"r");
    int t;
    fscanf(fp,"%d\n",&t);
    printf("The number of tasks are : %d \n", t);
    char type;
    int num;


}