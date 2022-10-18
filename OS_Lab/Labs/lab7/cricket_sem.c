#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sched.h>
#include <semaphore.h>

sem_t lock_sem1;
sem_t lock_sem2;
sem_t cond_sem1;
sem_t queue_sem1;
sem_t match_finished;
int matches=0;
int won_titan=0;
int won_capitals=0;
int highest_ind_score=0;
int highest_team_score=0;
int capital_counter=0;
int titans_counter=0;
int ready=0;


void player_thread(void* arg){
    
    sem_wait(&cond);
    ready++;
    if(ready==22){
        sem_post(&cond_sem1);
    }

}


void* main_thread_func(void* arg){
    while(true){
        sem_wait(&cond_finished);
    }
}




int main(int argc, char* argv[]){
    sem_init(&lock_sem1, 0, 1);
    sem_init(&lock_sem2, 0, 1);
    sem_init(&cond_sem1, 0, 0);
    sem_init(&queue_sem1, 0, 22);
    sem_init(&match_finished, 0, 0);
    if (argc != 2)
    {
        printf("Usage: ./cricket <number of threads>\n");
    }
    int n = atoi(argv[1]);
    pthread_t main_thread;
    pthread_t player_threads[n];

    pthread_create(&main_thread, NULL, &main_thread_func, NULL);
    for (int i = 0; i < n; i++)
    {
        pthread_create(&player_threads[i], NULL, &player_thread, NULL);
    }
}

