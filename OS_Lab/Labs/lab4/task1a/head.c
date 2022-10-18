#include "types.h"
#include "stat.h"
#include "user.h"

char buf[512];

void
cat(int fd, int lines)
{
    int a;
  if(lines<0){
    printf(1,"head: number of lines to be read must be positive\n");
    exit();
  }
  if(lines==0){
    return;
  }else{
    while(lines!=0 ){
      a=read(fd,buf,sizeof(buf));
      if(a==0){
        return;
      }else{
        for(int i=0;i<a;i++){
          if(lines>0){
            if(buf[i]=='\n'){
              printf(1,"%c",buf[i]);
              lines--;
            }else{
              printf(1,"%c",buf[i]);  
            }
          }else{
            return;
          }
        }
      }
    }
  }
  int n=lines;
  if(n < 0){
    printf(1, "cat: read error\n");
    exit();
  }
}

int
main(int argc, char *argv[])
//can i create a int* argv[] or int arg[] for taking integer arguments 
{
  int fd, i;

  if(argc <= 2){
    printf(1,"Please give input text file names\n");
    exit();
  }
  int lines = atoi(argv[1]);
  for(i = 2; i < argc; i++){
    if((fd = open(argv[i], 0)) < 0){
      printf(1, "head: cannot open %s\n", argv[i]);
      exit();
    }
    cat(fd,lines);
    close(fd);
  }
  exit();
}
