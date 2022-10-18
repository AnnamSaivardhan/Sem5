#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

sem_t queue_sem;
pthread_mutex_t first_lock;
pthread_cond_t players_filled;

// Global variables
int *arr;
int first = 0;
int total = 0;
int queued = 0;
int players_in = 0;
int matches = 0;
int won_titan = 0;
int won_capitals = 0;
int highest_ind_score = 0;
int highest_team_score = 0;
int capital_counter = 0;
int titans_counter = 0;

void get_to_queue(int id)
{
    sem_wait(&queue_sem);
    pthread_mutex_lock(&first_lock);
    arr[first] = id;
    first++;
    players_in++;
    pthread_mutex_unlock(&first_lock);
    if (players_in == 22)
    {
        pthread_cond_signal(&players_filled);
    }
}

void *main_thread_func(void *arg)
{
    while (true)
    {
        pthread_mutex_lock(&first_lock);
        while (players_in != 22)
        {
            pthread_cond_wait(&players_filled, &first_lock);
            if (players_in < 22)
            {
                printf("----------------------SUMMARY OF THE DAY-------------------------------\n");
                printf("Matches played:%d\n", matches);
                printf("Titans won:%d   Capitals won:%d  Tied matches: %d\n", won_titan, won_capitals, (matches - won_capitals - won_titan));
                printf("Highest team score:%d\n", highest_team_score);
                printf("Highest Individual score:%d\n", highest_ind_score);
            }
        }
        for(int i=0;i<11;i++){
            
        }
    }
}

void *player_thread(void *arg)
{
    int *id = (int *)arg;
    get_to_queue(id);
}

int main(int argc, int *argv[])
{
    sem_init(&queue_sem, 0, 22);
    pthread_mutex_init(&first_lock, NULL);
    pthread_cond_init(&players_filled, NULL);
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