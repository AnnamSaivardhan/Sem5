#include<stdio.h>
#include<signal.h>
#include<unistd.h>



int main(int arg,char* argv[]){
    char* a=argv[1];
    int pid=atoi(argv[1]);
    printf("SIGINT sent to pid: %d\n",pid);
    kill(pid,SIGINT);
    sleep(10);
    printf("SIGTERM sent to pid: %d\n",pid);
    kill(pid,SIGTERM);
    sleep(10);
    printf("SIGKILL sent to pid: %d\n",pid);
    kill(pid,SIGKILL);

}

// SIGINT - ctrl+c
//SISSEGV - segmentation fault
// kill -<signal> pid if no specific signal is specified then SIGTERM is sent

//We can also send from one program to another
//#include<sys/types.h>
//#include<signal.h>
//int kill(pid_t pid ,int sig)
/* To kill itself use if (kill(getpid(),SIGABRT))
                            exit(1);
equivalently int raise(int sig); == if(raise(SIGABRT)>0) exit(1); */



#define SIGHUP 1 /* Hangup (POSIX). */
#define SIGINT 2 /* Interrupt (ANSI). */
#define SIGQUIT 3 /* Quit (POSIX). */
#define SIGILL 4 /* Illegal instruction (ANSI). */
#define SIGTRAP 5 /* Trace trap (POSIX). */
#define SIGABRT 6 /* Abort (ANSI). */
#define SIGFPE 8 /* Floating-point exception (ANSI). */
#define SIGKILL 9 /* Kill, unblockable (POSIX). */
#define SIGUSR1 10 /* User-defined signal 1 (POSIX). */
#define SIGSEGV 11 /* Segmentation violation (ANSI). */
#define SIGUSR2 12 /* User-defined signal 2 (POSIX). */
#define SIGPIPE 13 /* Broken pipe (POSIX). */
#define SIGALRM 14 /* Alarm clock (POSIX). */
#define SIGTERM 15 /* Termination (ANSI). */
#define SIGCHLD 17 /* Child status has changed (POSIX). */
#define SIGCONT 18 /* Continue (POSIX). */
#define SIGSTOP 19 /* Stop, unblockable (POSIX). */
#define SIGTSTP 20 /* Keyboard stop (POSIX). */
#define SIGTTIN 21 /* Background read from tty (POSIX). */
#define SIGTTOU 22 /* Background write to tty (POSIX). */
#define SIGPROF 27 /* Profiling alarm clock (4.2 BSD).   */ 


// two signals are not catchablw in user program -> KILL ->STOP
//to install handler use include<signal.h>

