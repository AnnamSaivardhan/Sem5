#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/*
While giving address of a cahr array to printf give the address of first element
method 1: &arr[0]
method 2: arr
Note: arr[], &arr is wrong

if we create a an array buf[7] then we get a array with each element as random, some will be '\0'(but buf[7] will be '\0' for sure) and some are garbage values, when we try to print char array as string, it stops when it reaches '\0' so it may print some garbage values in between

if we modified buf[0] to buf[6] except buf[3] then while printing the string may stop at buf[3] because it may encounters  a '\0' at buf[3]

we cannot modify buf[7] to buf[7+8](i.e 8 bytes after our arra ends) if you does that the we will get a stack smashed error

*/
int main(){
    char buf[7];
    buf[0]='s';
    buf[1]='a';
    buf[2]='i';
    //buf[3]='v';
    buf[3]='d';
    buf[4]='h';
    buf[5]='a';
    buf[6]='\0';
    //buf[7]='h';
   // buf[17]='\0';
   // printf("%c",buf[9]);
    printf("%s\n",buf);
    
}