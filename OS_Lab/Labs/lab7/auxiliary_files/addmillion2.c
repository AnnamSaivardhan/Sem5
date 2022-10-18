#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include<sys/wait.h>
#include<fcntl.h>
#include<stdlib.h>
#include<sys/stat.h>
#include <pthread.h>
#include<time.h>

int account_balance = 0;
pthread_mutex_t lk = PTHREAD_MUTEX_INITIALIZER;
//pthread_mutex_init(lk);// Can't we use this??????

void* increment(void* arg) {
    //printf("hi\n");
    int * money = (int*)arg;
    for (int i = 0; i < 1000000*(*money); i++) {
        pthread_mutex_lock(&lk);
        account_balance++;
        if(account_balance>1000000 && account_balance%1000000==0) printf("%d\n",account_balance);
        pthread_mutex_unlock(&lk);
    }
}

int main(int argc, char* argv[]) {
    clock_t start,end;
    double cpu_time_used;
    start = clock();
    int threadNum = atoi(argv[1]);
    int money = (2048)/threadNum;
    pthread_t th[threadNum];
    int i;
    for (i = 0; i < threadNum; i++) {
        if (pthread_create(th + i, NULL, &increment, (void*)&money) != 0) {
            perror("Failed to create thread");
            return 1;
        }
        //printf("Transaction %d has started\n", i);
    }
    for (i = 0; i < threadNum; i++) {
        //printf("hello\n");
        // int z=pthread_join(th[i], NULL);
        // printf("%d\n",z);
        if (pthread_join(th[i], NULL) != 0) {
            return 2;
        }
        //printf("Transaction %d has finished\n", i);
    }
    
    //printf("Account Balance is : %d\n", account_balance);
    end = clock();
    cpu_time_used = ((double)(end-start))/CLOCKS_PER_SEC;
    printf("Time spent: %f ms\n",cpu_time_used);
    return 0;
}