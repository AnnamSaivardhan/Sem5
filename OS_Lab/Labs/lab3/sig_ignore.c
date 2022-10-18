#include<stdio.h>
#include<signal.h>
#include<unistd.h>



int main(){
    printf("Process ID is: %d\n",getpid());
    signal(SIGINT, SIG_IGN); //SIG_IGN says to ignore the signal
    signal(SIGTERM,SIG_IGN); 
    while(1){
        printf("Waiting...\n");
        sleep(3);
    }

}

// Types of signalsBACK TO TOC
// SIGHUP
// This signal indicates that someone has killed the controlling terminal. For instance, lets say our program runs in xterm or in gnome-terminal. When someone kills the terminal program, without killing applications running inside of terminal window, operating system sends SIGHUP to the program. Default handler for this signal will terminate your program.
// Thanks to Mark Pettit for the tip.

// SIGINT
// This is the signal that being sent to your application when it is running in a foreground in a terminal and someone presses CTRL-C. Default handler of this signal will quietly terminate your program.

// SIGQUIT
// Again, according to documentation, this signal means “Quit from keyboard”. In reality I couldn’t find who sends this signal. I.e. you can only send it explicitly.

// SIGILL
// Illegal instruction signal. This is a exception signal, sent to your application by the operating system when it encounters an illegal instruction inside of your program. Something like this may happen when executable file of your program has been corrupted. Another option is when your program loads dynamic library that has been corrupted. Consider this as an exception of a kind, but the one that is very unlikely to happen.

// SIGABRT
// Abort signal means you used used abort() API inside of your program. It is yet another method to terminate your program. abort() issues SIGABRT signal which in its term terminates your program (unless handled by your custom handler). It is up to you to decide whether you want to use abort() or not.

// SIGFPE
// Floating point exception. This is another exception signal, issued by operating system when your application caused an exception.

// SIGSEGV
// This is an exception signal as well. Operating system sends a program this signal when it tries to access memory that does not belong to it.

// SIGPIPE
// Broken pipe. As documentation states, this signal sent to your program when you try to write into pipe (another IPC) with no readers on the other side.

// SIGALRM
// Alarm signal. Sent to your program using alarm() system call. The alarm() system call is basically a timer that allows you to receive SIGALRM in preconfigured number of seconds. This can be handy, although there are more accurate timer API out there.

// SIGTERM
// This signal tells your program to terminate itself. Consider this as a signal to cleanly shut down while SIGKILL is an abnormal termination signal.

// SIGCHLD
// Tells you that a child process of your program has stopped or terminated. This is handy when you wish to synchronize your process with a process with its child.

// SIGUSR1 and SIGUSR2
// Finally, SIGUSR1 and SIGUSR2 are two signals that have no predefined meaning and are left for your consideration. You may use these signals to synchronise your program with some other program or to communicate with it.