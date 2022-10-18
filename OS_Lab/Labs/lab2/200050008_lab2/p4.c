#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include<sys/wait.h>
#include<fcntl.h>
#include<stdlib.h>
#include<sys/stat.h>
//treating char array as string is dangerous
//Whenever you create a char array change evry variable of that array to '\0'

int main(){
    //opening the file into file in to file descriptor
    //fd1 stores the file descriptor number
    int fd1 = open("f1.txt",O_RDONLY);
    printf("file descriptor number of f1:%d\n",fd1);
    int fd2 = open("f2.txt",O_RDWR);    
    printf("file descriptor number of f2:%d\n",fd2);



    //Reading from file descriptor to array

    //this ensures that every element is '\0'
    char buf[100]={'\0'}; 

    //Reading from file derciptor to buf array it will read min(size of file in fd, 25(amount of bytes it was asked to read))
    int size = read(fd1,buf,25); 
    /*If the buffer size is less than number of bytes in text file then put while(size = read(fd1,buf,n) >0)
       then the while loop runs until every byte is read from file. This implementation is working becuase
       read commands removes data from file_descriptor while reading data from it.
    */
    /*
    even if we mentoined to take 25 bytes it will only read until the end of the file decriptor and returns the number of bytes it read
    */
    printf("size read from fd1:%d\n",size);
    printf("string received from fd1:%s\n",buf);


    //Writing from buf to f2.txt
    int size2 = write(fd2,buf,size);
    /*
    Here you should be careful we need to provide exact amount of bytes to be read other wise it reads extra characters
    */


    //closing file decriptors
    close(fd1);
    close(fd2);


}
// int main(){

    






//     char a[50];
//     char b[50];
//     char *c;
//     scanf("%s",a);
//     scanf("%s",b);
//     int fd1=open(a,O_RDONLY);
//     int fd2=open(b,O_RDWR);
//     //int fd3=open("abc.txt",O_RDWR);
//     // printf("%d\n",fd1);
//     // printf("%d\n",fd2);
//     // printf("%d\n",fd3);
//     read(fd1,c,sizeof(a));
//     printf("%s\n",c);
//     write(fd2,c,sizeof(a));
//     close(fd1);
//     close(fd2);


// }