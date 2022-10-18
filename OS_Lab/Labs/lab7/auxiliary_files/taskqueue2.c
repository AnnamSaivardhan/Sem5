#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sched.h>

pthread_mutex_t lk = PTHREAD_MUTEX_INITIALIZER;


typedef struct{
    long number;
    int index;
    int* addr;
}my_arg;

// Global variables
long sum = 0;
long odd = 0;
long even = 0;
long min = INT_MAX;
long max = INT_MIN;
bool done = false;

void assigntask(pthread_t* pid){
    
}

void* processtask(void* args);

void* processtask(void* args)
{
    //printf("hi\n");
    //printf("hello\n");
    my_arg* new = (my_arg*)args;
    long number = new->number ;
    // simulate burst time
    sleep(number);

    // update global variables
    pthread_mutex_lock(&lk);
    sum += number;
    if (number % 2 == 1)
    {
        odd++;
    }
    else
    {
        even++;
    }
    if (number < min)
    {
        min = number;
    }
    if (number > max)
    {
        max = number;
    }
    printf("Task completed\n");
    pthread_mutex_unlock(&lk);
    
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: sum <infile>\n");
        exit(EXIT_FAILURE);
    }
    int num_threads = atoi(argv[1]);
    char *fn = argv[2];
    // Read from file
    FILE *fin = fopen(fn, "r");
    long t;
    fscanf(fin, "%ld\n", &t);
    printf("The number of tasks are : %ld \n", t);
    char type;
    long num;
    int free = num_threads;
    int first = 0;
    int active[num_threads];
    int rets[num_threads];
    for(int i=0;i<num_threads;i++){
        active[i]=0;
    }
    bool avail = 1;
    pthread_t pid[num_threads];
    my_arg args[num_threads];

    while (fscanf(fin, "%c %ld\n", &type, &num) == 2)
    {   
        avail=0;
        while(avail==0){
            //printf("z\n");
        for(int i=0;i<num_threads;i++){
            if(active[i]==0){
                //printf("y %d\n",i);
                //pthread_join(pid[i],NULL);
                //printf("t %d\n",i);
                avail=1;
                first = i;
                break;
            }
            
            
        }
        
         if(avail==0){
            //printf("zzzz\n");
            sched_yield();
        }
        
        }
        
       
        
        if(type=='p'){
            //printf("zzzz\n");
            args[first].number = num;
            args[first].index = first;
            args[first].addr = &active[first];
            active[first]=1;
            //printf("zzzz\n");
            int z = pthread_create(&pid[first],NULL,processtask,(void*)&args[first]);
            //printf("hh %d\n",z);
        }else{
            sleep(num);
            printf("Wait Over\n");
        }
      
    }
    fclose(fin);
    bool final = 0;
    for(int i=0;i<num_threads;i++){
        pthread_join(pid[i],NULL);
    }

    // Print global variables
    printf("%ld %ld %ld %ld %ld\n", sum, odd, even, min, max);

    return (EXIT_SUCCESS);
}
