#include "types.h"
#include "stat.h"
#include "user.h"

char buf[512];

void
cat(int fd, int z)
{
  int n;

  while((n = read(fd, buf, sizeof(buf))) > 0) {
    // if (write(1, buf, n) != n) {
    //   printf(1, "cat: write error\n");
    //   exit();
    // }
    for(int i=0;i<n;i++){
      if(z>0){
        printf(1,"%c",buf[i]);
        if(buf[i]=='\n'){
          
          z--;
        }
      }
    }
  }
  if(n < 0){
    printf(1, "cat: read error\n");
    exit();
  }
}

int
main(int argc, char *argv[])
{
  int fd, i;

  if(argc <= 1){
    cat(0,0);
    exit();
  }

  for(i = 2; i < argc; i++){
    int z = atoi(argv[1]);
    //printf(1,argv[1]);
    if((fd = open(argv[i], 0)) < 0){
      printf(1, "cat: cannot open %s\n", argv[i]);
      exit();
    }
    cat(fd,z);
    close(fd);
  }
  exit();
}
