#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Global variables
int sum = 0;
int odd = 0;
int even = 0;
int min = INT_MAX;
int max = INT_MIN;

typedef struct
{
    int tm;
    char type;
} my_arg;

int *it_arr;
char *cr_arr;
int first = -1;
int last = -1;
int done = 0;
int total;
pthread_mutex_t lk = PTHREAD_MUTEX_INITIALIZER;  // Accessing queue
pthread_mutex_t lk2 = PTHREAD_MUTEX_INITIALIZER; // Accessing sum variables
pthread_mutex_t lk3 = PTHREAD_MUTEX_INITIALIZER; // Accessing for done variable
pthread_cond_t cond1 = PTHREAD_COND_INITIALIZER; // condition for parent to wait
pthread_cond_t cond2 = PTHREAD_COND_INITIALIZER; // condition for children to wait
pthread_cond_t cond3 = PTHREAD_COND_INITIALIZER; // condition for parent to exit

void put(char type, int time)
{
    pthread_mutex_lock(&lk);
    while (last == (first + 4) % 5)
    {
        pthread_cond_wait(&cond1, &lk);
    }
    if (first == -1)
    {
        it_arr[0] = time;
        cr_arr[0] = type;
        first = 0;
        last = 0;
    }
    else
    {
        it_arr[last + 1] = time;
        cr_arr[last + 1] = type;
        last = (last + 1) % 5;
    }
    pthread_cond_signal(&cond2);
    pthread_mutex_unlock(&lk);
    // printf("put succeded\n");
}

void take(my_arg *arg)
{
    pthread_mutex_lock(&lk);
    while (first == -1)
    {
        pthread_cond_wait(&cond2, &lk);
    }
    if (first == last)
    {
        arg->tm = it_arr[first];
        arg->type = cr_arr[first];
        first = -1;
        last = -1;
    }
    else
    {
        arg->tm = it_arr[first];
        arg->type = cr_arr[first];
        first = (first + 1) % 5;
    }
    pthread_cond_signal(&cond1);
    pthread_mutex_unlock(&lk);
    // printf("%ckdhgjkh%d\n",arg->type,arg->tm);
    // printf("take succedded\n");
}

void *thread_func()
{
    my_arg args;
    while (true)
    {
        take(&args);
        if (args.type == 'p')
        {
            sleep(args.tm);
            int number = args.tm;
            pthread_mutex_lock(&lk2);
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
            pthread_mutex_unlock(&lk2);
        }
        else if (args.type == 'w')
        {
            int number = args.tm;
            sleep(number);
            printf("Wait Over\n");
        }

        pthread_mutex_lock(&lk3);
        done++;
        if (total == done)
        {   printf("heyy\n");
            pthread_cond_signal(&cond3);
        }
        pthread_mutex_unlock(&lk3);
    }
}

int main(int argc, char *argv[])
{
    it_arr = malloc(5 * sizeof(int));
    cr_arr = malloc(5 * sizeof(char));
    if (argc != 3)
    {
        printf("Usage: sum <infile> <number_of_threads>\n");
        exit(EXIT_FAILURE);
    }
    pthread_t id[atoi(argv[2])];
    for (int k = 0; k < atoi(argv[2]); k++)
    {
        pthread_create(&id[k], NULL, thread_func, NULL);
    }
    printf("threads created\n");
    char *fn = argv[1];
    // Read from file
    FILE *fin = fopen(fn, "r");
    int t;
    fscanf(fin, "%d\n", &t);
    total = t;
    printf("The number of tasks are : %d \n", t);
    char type;
    int num;
    while (fscanf(fin, "%c %d\n", &type, &num) == 2)
    {
        printf("%c %d\n",type,num);
        put(type, num);
        // printf("put main\n");
    }
    fclose(fin);
    pthread_mutex_lock(&lk3);
    while (done != total)
    {
        pthread_cond_wait(&cond3, &lk3);
    }
    pthread_mutex_unlock(&lk3);
    printf("%d %d %d %d %d\n", sum, odd, even, min, max);

    return (EXIT_SUCCESS);
}
