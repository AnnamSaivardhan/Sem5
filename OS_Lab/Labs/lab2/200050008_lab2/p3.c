// Write a program p3.c that prints a prompt (">>> ") and takes as input the name of an executable
// program located in the same folder. Next, p3.c should first call fork and from within the child process call
// a variant of exec with the specified program to execute the new program.
// The parent process should fallback to the prompt and wait for input specifying the name of another
// executable to execute (and repeat).
// For example,
// Consider two executable programs helloworld and byeworld located in the same folder.
// Prompt ">>> " should be printed before the user input is read
// and then the name of the executable provided should be executed.
// Sample output:
// >>> helloworld
// this is hello world program
// >>> byeworld
// this is bye world program
// >>> ^C
// You should be able to close this program using Ctrl + C.
// Note: The name of the program at input prompt should not exceed 50 characters.
/*
execl   - It takes list of arguments and we need to mention the path 
execlp  - We don't need to mention path

exeecvp - we just give filename , no need to give path for it and we give argument list instead of giving each argument explicitly.
int execvp (const char *file, char *const argv[]);


*/


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<sys/wait.h>

int main(){
    while(1){
        printf(">>>");
        char program[50];
        scanf("%s", program);
        pid_t pid = fork();
        if(pid == 0){
            char* name="ls";
           char* arg1[3];
           arg1[0]= "abc.txt";
            arg1[1]="/home/saivardhan/Documents";
            execlp(name,name, NULL);
            
            //printf("execution done from pid %d",getpid());
            exit(0);
        }
        else{
            wait(NULL);
        }
    }
    return 0;
}