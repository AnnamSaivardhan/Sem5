
_test1:     file format elf32-i386


Disassembly of section .text:

00000000 <main>:
#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

int main(int argc, char *argv[]) {
   0:	8d 4c 24 04          	lea    0x4(%esp),%ecx
   4:	83 e4 f0             	and    $0xfffffff0,%esp
   7:	ff 71 fc             	push   -0x4(%ecx)
   a:	55                   	push   %ebp
   b:	89 e5                	mov    %esp,%ebp
   d:	51                   	push   %ecx
   e:	83 ec 54             	sub    $0x54,%esp
  11:	89 c8                	mov    %ecx,%eax

    int NCHILD;

    if(argc<2)
  13:	83 38 01             	cmpl   $0x1,(%eax)
  16:	7f 09                	jg     21 <main+0x21>
        NCHILD = 2;
  18:	c7 45 f4 02 00 00 00 	movl   $0x2,-0xc(%ebp)
  1f:	eb 14                	jmp    35 <main+0x35>
    else 
        NCHILD = argv[1][0] - '0';
  21:	8b 40 04             	mov    0x4(%eax),%eax
  24:	83 c0 04             	add    $0x4,%eax
  27:	8b 00                	mov    (%eax),%eax
  29:	0f b6 00             	movzbl (%eax),%eax
  2c:	0f be c0             	movsbl %al,%eax
  2f:	83 e8 30             	sub    $0x30,%eax
  32:	89 45 f4             	mov    %eax,-0xc(%ebp)

    printf(1, "*Case1: Parent has no children*\n");
  35:	83 ec 08             	sub    $0x8,%esp
  38:	68 60 09 00 00       	push   $0x960
  3d:	6a 01                	push   $0x1
  3f:	e8 5e 05 00 00       	call   5a2 <printf>
  44:	83 c4 10             	add    $0x10,%esp
    int wtime1, rtime1;
    int status = wait2(&wtime1, &rtime1);
  47:	83 ec 08             	sub    $0x8,%esp
  4a:	8d 45 dc             	lea    -0x24(%ebp),%eax
  4d:	50                   	push   %eax
  4e:	8d 45 e0             	lea    -0x20(%ebp),%eax
  51:	50                   	push   %eax
  52:	e8 6f 04 00 00       	call   4c6 <wait2>
  57:	83 c4 10             	add    $0x10,%esp
  5a:	89 45 e8             	mov    %eax,-0x18(%ebp)

    if(status == -1) {
  5d:	83 7d e8 ff          	cmpl   $0xffffffff,-0x18(%ebp)
  61:	75 17                	jne    7a <main+0x7a>
        printf(1, "wait2 status: %d\n", status);
  63:	83 ec 04             	sub    $0x4,%esp
  66:	ff 75 e8             	push   -0x18(%ebp)
  69:	68 81 09 00 00       	push   $0x981
  6e:	6a 01                	push   $0x1
  70:	e8 2d 05 00 00       	call   5a2 <printf>
  75:	83 c4 10             	add    $0x10,%esp
  78:	eb 12                	jmp    8c <main+0x8c>
    } else {
        printf(1, "wait2 should return -1 if calling process has no children\n");
  7a:	83 ec 08             	sub    $0x8,%esp
  7d:	68 94 09 00 00       	push   $0x994
  82:	6a 01                	push   $0x1
  84:	e8 19 05 00 00       	call   5a2 <printf>
  89:	83 c4 10             	add    $0x10,%esp
    }


    printf(1, "*Case2: Parent has children*\n");
  8c:	83 ec 08             	sub    $0x8,%esp
  8f:	68 cf 09 00 00       	push   $0x9cf
  94:	6a 01                	push   $0x1
  96:	e8 07 05 00 00       	call   5a2 <printf>
  9b:	83 c4 10             	add    $0x10,%esp
    for ( int child = 0; child < NCHILD; child++ ) {
  9e:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
  a5:	e9 c6 00 00 00       	jmp    170 <main+0x170>
        int pid = fork ();
  aa:	e8 6f 03 00 00       	call   41e <fork>
  af:	89 45 e4             	mov    %eax,-0x1c(%ebp)
        if ( pid < 0 ) {
  b2:	83 7d e4 00          	cmpl   $0x0,-0x1c(%ebp)
  b6:	79 1d                	jns    d5 <main+0xd5>
            printf(1, "%d failed in fork!\n", getpid());
  b8:	e8 e9 03 00 00       	call   4a6 <getpid>
  bd:	83 ec 04             	sub    $0x4,%esp
  c0:	50                   	push   %eax
  c1:	68 ed 09 00 00       	push   $0x9ed
  c6:	6a 01                	push   $0x1
  c8:	e8 d5 04 00 00       	call   5a2 <printf>
  cd:	83 c4 10             	add    $0x10,%esp
            exit();
  d0:	e8 51 03 00 00       	call   426 <exit>
        } else if (pid == 0) {
  d5:	83 7d e4 00          	cmpl   $0x0,-0x1c(%ebp)
  d9:	0f 85 8d 00 00 00    	jne    16c <main+0x16c>
            sleep(100);
  df:	83 ec 0c             	sub    $0xc,%esp
  e2:	6a 64                	push   $0x64
  e4:	e8 cd 03 00 00       	call   4b6 <sleep>
  e9:	83 c4 10             	add    $0x10,%esp
            printf(1, "Child %d created\n",getpid());
  ec:	e8 b5 03 00 00       	call   4a6 <getpid>
  f1:	83 ec 04             	sub    $0x4,%esp
  f4:	50                   	push   %eax
  f5:	68 01 0a 00 00       	push   $0xa01
  fa:	6a 01                	push   $0x1
  fc:	e8 a1 04 00 00       	call   5a2 <printf>
 101:	83 c4 10             	add    $0x10,%esp
            volatile double a, b;
            a = 3.14;
 104:	dd 05 80 0a 00 00    	fldl   0xa80
 10a:	dd 5d c8             	fstpl  -0x38(%ebp)
            b = 36.29;
 10d:	dd 05 88 0a 00 00    	fldl   0xa88
 113:	dd 5d c0             	fstpl  -0x40(%ebp)
            volatile double x = 0, z;
 116:	d9 ee                	fldz   
 118:	dd 5d b8             	fstpl  -0x48(%ebp)
            for (z = 0; z < 90000.0; z += 0.1)
 11b:	d9 ee                	fldz   
 11d:	dd 5d b0             	fstpl  -0x50(%ebp)
 120:	eb 1e                	jmp    140 <main+0x140>
            {
                x = x + a * b; 
 122:	dd 45 c8             	fldl   -0x38(%ebp)
 125:	dd 45 c0             	fldl   -0x40(%ebp)
 128:	de c9                	fmulp  %st,%st(1)
 12a:	dd 45 b8             	fldl   -0x48(%ebp)
 12d:	de c1                	faddp  %st,%st(1)
 12f:	dd 5d b8             	fstpl  -0x48(%ebp)
            for (z = 0; z < 90000.0; z += 0.1)
 132:	dd 45 b0             	fldl   -0x50(%ebp)
 135:	dd 05 90 0a 00 00    	fldl   0xa90
 13b:	de c1                	faddp  %st,%st(1)
 13d:	dd 5d b0             	fstpl  -0x50(%ebp)
 140:	dd 45 b0             	fldl   -0x50(%ebp)
 143:	dd 05 98 0a 00 00    	fldl   0xa98
 149:	df f1                	fcomip %st(1),%st
 14b:	dd d8                	fstp   %st(0)
 14d:	77 d3                	ja     122 <main+0x122>
            }
            printf(1, "Child %d finished\n",getpid());
 14f:	e8 52 03 00 00       	call   4a6 <getpid>
 154:	83 ec 04             	sub    $0x4,%esp
 157:	50                   	push   %eax
 158:	68 13 0a 00 00       	push   $0xa13
 15d:	6a 01                	push   $0x1
 15f:	e8 3e 04 00 00       	call   5a2 <printf>
 164:	83 c4 10             	add    $0x10,%esp
            exit();
 167:	e8 ba 02 00 00       	call   426 <exit>
    for ( int child = 0; child < NCHILD; child++ ) {
 16c:	83 45 f0 01          	addl   $0x1,-0x10(%ebp)
 170:	8b 45 f0             	mov    -0x10(%ebp),%eax
 173:	3b 45 f4             	cmp    -0xc(%ebp),%eax
 176:	0f 8c 2e ff ff ff    	jl     aa <main+0xaa>
        }
    }
    int wtime, rtime;
    for(int i=0; i<NCHILD; i++){
 17c:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
 183:	eb 3d                	jmp    1c2 <main+0x1c2>
        status = wait2(&wtime, &rtime);
 185:	83 ec 08             	sub    $0x8,%esp
 188:	8d 45 d4             	lea    -0x2c(%ebp),%eax
 18b:	50                   	push   %eax
 18c:	8d 45 d8             	lea    -0x28(%ebp),%eax
 18f:	50                   	push   %eax
 190:	e8 31 03 00 00       	call   4c6 <wait2>
 195:	83 c4 10             	add    $0x10,%esp
 198:	89 45 e8             	mov    %eax,-0x18(%ebp)
        printf(1, "Child no. %d, Child pid: %d exited with Status: %d, Waiting Time: %d, Run Time: %d\n", i, status, status, wtime, rtime);
 19b:	8b 55 d4             	mov    -0x2c(%ebp),%edx
 19e:	8b 45 d8             	mov    -0x28(%ebp),%eax
 1a1:	83 ec 04             	sub    $0x4,%esp
 1a4:	52                   	push   %edx
 1a5:	50                   	push   %eax
 1a6:	ff 75 e8             	push   -0x18(%ebp)
 1a9:	ff 75 e8             	push   -0x18(%ebp)
 1ac:	ff 75 ec             	push   -0x14(%ebp)
 1af:	68 28 0a 00 00       	push   $0xa28
 1b4:	6a 01                	push   $0x1
 1b6:	e8 e7 03 00 00       	call   5a2 <printf>
 1bb:	83 c4 20             	add    $0x20,%esp
    for(int i=0; i<NCHILD; i++){
 1be:	83 45 ec 01          	addl   $0x1,-0x14(%ebp)
 1c2:	8b 45 ec             	mov    -0x14(%ebp),%eax
 1c5:	3b 45 f4             	cmp    -0xc(%ebp),%eax
 1c8:	7c bb                	jl     185 <main+0x185>
    }
    exit();
 1ca:	e8 57 02 00 00       	call   426 <exit>

000001cf <stosb>:
               "cc");
}

static inline void
stosb(void *addr, int data, int cnt)
{
 1cf:	55                   	push   %ebp
 1d0:	89 e5                	mov    %esp,%ebp
 1d2:	57                   	push   %edi
 1d3:	53                   	push   %ebx
  asm volatile("cld; rep stosb" :
 1d4:	8b 4d 08             	mov    0x8(%ebp),%ecx
 1d7:	8b 55 10             	mov    0x10(%ebp),%edx
 1da:	8b 45 0c             	mov    0xc(%ebp),%eax
 1dd:	89 cb                	mov    %ecx,%ebx
 1df:	89 df                	mov    %ebx,%edi
 1e1:	89 d1                	mov    %edx,%ecx
 1e3:	fc                   	cld    
 1e4:	f3 aa                	rep stos %al,%es:(%edi)
 1e6:	89 ca                	mov    %ecx,%edx
 1e8:	89 fb                	mov    %edi,%ebx
 1ea:	89 5d 08             	mov    %ebx,0x8(%ebp)
 1ed:	89 55 10             	mov    %edx,0x10(%ebp)
               "=D" (addr), "=c" (cnt) :
               "0" (addr), "1" (cnt), "a" (data) :
               "memory", "cc");
}
 1f0:	90                   	nop
 1f1:	5b                   	pop    %ebx
 1f2:	5f                   	pop    %edi
 1f3:	5d                   	pop    %ebp
 1f4:	c3                   	ret    

000001f5 <strcpy>:
#include "user.h"
#include "x86.h"

char*
strcpy(char *s, const char *t)
{
 1f5:	55                   	push   %ebp
 1f6:	89 e5                	mov    %esp,%ebp
 1f8:	83 ec 10             	sub    $0x10,%esp
  char *os;

  os = s;
 1fb:	8b 45 08             	mov    0x8(%ebp),%eax
 1fe:	89 45 fc             	mov    %eax,-0x4(%ebp)
  while((*s++ = *t++) != 0)
 201:	90                   	nop
 202:	8b 55 0c             	mov    0xc(%ebp),%edx
 205:	8d 42 01             	lea    0x1(%edx),%eax
 208:	89 45 0c             	mov    %eax,0xc(%ebp)
 20b:	8b 45 08             	mov    0x8(%ebp),%eax
 20e:	8d 48 01             	lea    0x1(%eax),%ecx
 211:	89 4d 08             	mov    %ecx,0x8(%ebp)
 214:	0f b6 12             	movzbl (%edx),%edx
 217:	88 10                	mov    %dl,(%eax)
 219:	0f b6 00             	movzbl (%eax),%eax
 21c:	84 c0                	test   %al,%al
 21e:	75 e2                	jne    202 <strcpy+0xd>
    ;
  return os;
 220:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 223:	c9                   	leave  
 224:	c3                   	ret    

00000225 <strcmp>:

int
strcmp(const char *p, const char *q)
{
 225:	55                   	push   %ebp
 226:	89 e5                	mov    %esp,%ebp
  while(*p && *p == *q)
 228:	eb 08                	jmp    232 <strcmp+0xd>
    p++, q++;
 22a:	83 45 08 01          	addl   $0x1,0x8(%ebp)
 22e:	83 45 0c 01          	addl   $0x1,0xc(%ebp)
  while(*p && *p == *q)
 232:	8b 45 08             	mov    0x8(%ebp),%eax
 235:	0f b6 00             	movzbl (%eax),%eax
 238:	84 c0                	test   %al,%al
 23a:	74 10                	je     24c <strcmp+0x27>
 23c:	8b 45 08             	mov    0x8(%ebp),%eax
 23f:	0f b6 10             	movzbl (%eax),%edx
 242:	8b 45 0c             	mov    0xc(%ebp),%eax
 245:	0f b6 00             	movzbl (%eax),%eax
 248:	38 c2                	cmp    %al,%dl
 24a:	74 de                	je     22a <strcmp+0x5>
  return (uchar)*p - (uchar)*q;
 24c:	8b 45 08             	mov    0x8(%ebp),%eax
 24f:	0f b6 00             	movzbl (%eax),%eax
 252:	0f b6 d0             	movzbl %al,%edx
 255:	8b 45 0c             	mov    0xc(%ebp),%eax
 258:	0f b6 00             	movzbl (%eax),%eax
 25b:	0f b6 c8             	movzbl %al,%ecx
 25e:	89 d0                	mov    %edx,%eax
 260:	29 c8                	sub    %ecx,%eax
}
 262:	5d                   	pop    %ebp
 263:	c3                   	ret    

00000264 <strlen>:

uint
strlen(const char *s)
{
 264:	55                   	push   %ebp
 265:	89 e5                	mov    %esp,%ebp
 267:	83 ec 10             	sub    $0x10,%esp
  int n;

  for(n = 0; s[n]; n++)
 26a:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 271:	eb 04                	jmp    277 <strlen+0x13>
 273:	83 45 fc 01          	addl   $0x1,-0x4(%ebp)
 277:	8b 55 fc             	mov    -0x4(%ebp),%edx
 27a:	8b 45 08             	mov    0x8(%ebp),%eax
 27d:	01 d0                	add    %edx,%eax
 27f:	0f b6 00             	movzbl (%eax),%eax
 282:	84 c0                	test   %al,%al
 284:	75 ed                	jne    273 <strlen+0xf>
    ;
  return n;
 286:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 289:	c9                   	leave  
 28a:	c3                   	ret    

0000028b <memset>:

void*
memset(void *dst, int c, uint n)
{
 28b:	55                   	push   %ebp
 28c:	89 e5                	mov    %esp,%ebp
  stosb(dst, c, n);
 28e:	8b 45 10             	mov    0x10(%ebp),%eax
 291:	50                   	push   %eax
 292:	ff 75 0c             	push   0xc(%ebp)
 295:	ff 75 08             	push   0x8(%ebp)
 298:	e8 32 ff ff ff       	call   1cf <stosb>
 29d:	83 c4 0c             	add    $0xc,%esp
  return dst;
 2a0:	8b 45 08             	mov    0x8(%ebp),%eax
}
 2a3:	c9                   	leave  
 2a4:	c3                   	ret    

000002a5 <strchr>:

char*
strchr(const char *s, char c)
{
 2a5:	55                   	push   %ebp
 2a6:	89 e5                	mov    %esp,%ebp
 2a8:	83 ec 04             	sub    $0x4,%esp
 2ab:	8b 45 0c             	mov    0xc(%ebp),%eax
 2ae:	88 45 fc             	mov    %al,-0x4(%ebp)
  for(; *s; s++)
 2b1:	eb 14                	jmp    2c7 <strchr+0x22>
    if(*s == c)
 2b3:	8b 45 08             	mov    0x8(%ebp),%eax
 2b6:	0f b6 00             	movzbl (%eax),%eax
 2b9:	38 45 fc             	cmp    %al,-0x4(%ebp)
 2bc:	75 05                	jne    2c3 <strchr+0x1e>
      return (char*)s;
 2be:	8b 45 08             	mov    0x8(%ebp),%eax
 2c1:	eb 13                	jmp    2d6 <strchr+0x31>
  for(; *s; s++)
 2c3:	83 45 08 01          	addl   $0x1,0x8(%ebp)
 2c7:	8b 45 08             	mov    0x8(%ebp),%eax
 2ca:	0f b6 00             	movzbl (%eax),%eax
 2cd:	84 c0                	test   %al,%al
 2cf:	75 e2                	jne    2b3 <strchr+0xe>
  return 0;
 2d1:	b8 00 00 00 00       	mov    $0x0,%eax
}
 2d6:	c9                   	leave  
 2d7:	c3                   	ret    

000002d8 <gets>:

char*
gets(char *buf, int max)
{
 2d8:	55                   	push   %ebp
 2d9:	89 e5                	mov    %esp,%ebp
 2db:	83 ec 18             	sub    $0x18,%esp
  int i, cc;
  char c;

  for(i=0; i+1 < max; ){
 2de:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
 2e5:	eb 42                	jmp    329 <gets+0x51>
    cc = read(0, &c, 1);
 2e7:	83 ec 04             	sub    $0x4,%esp
 2ea:	6a 01                	push   $0x1
 2ec:	8d 45 ef             	lea    -0x11(%ebp),%eax
 2ef:	50                   	push   %eax
 2f0:	6a 00                	push   $0x0
 2f2:	e8 47 01 00 00       	call   43e <read>
 2f7:	83 c4 10             	add    $0x10,%esp
 2fa:	89 45 f0             	mov    %eax,-0x10(%ebp)
    if(cc < 1)
 2fd:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 301:	7e 33                	jle    336 <gets+0x5e>
      break;
    buf[i++] = c;
 303:	8b 45 f4             	mov    -0xc(%ebp),%eax
 306:	8d 50 01             	lea    0x1(%eax),%edx
 309:	89 55 f4             	mov    %edx,-0xc(%ebp)
 30c:	89 c2                	mov    %eax,%edx
 30e:	8b 45 08             	mov    0x8(%ebp),%eax
 311:	01 c2                	add    %eax,%edx
 313:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 317:	88 02                	mov    %al,(%edx)
    if(c == '\n' || c == '\r')
 319:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 31d:	3c 0a                	cmp    $0xa,%al
 31f:	74 16                	je     337 <gets+0x5f>
 321:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 325:	3c 0d                	cmp    $0xd,%al
 327:	74 0e                	je     337 <gets+0x5f>
  for(i=0; i+1 < max; ){
 329:	8b 45 f4             	mov    -0xc(%ebp),%eax
 32c:	83 c0 01             	add    $0x1,%eax
 32f:	39 45 0c             	cmp    %eax,0xc(%ebp)
 332:	7f b3                	jg     2e7 <gets+0xf>
 334:	eb 01                	jmp    337 <gets+0x5f>
      break;
 336:	90                   	nop
      break;
  }
  buf[i] = '\0';
 337:	8b 55 f4             	mov    -0xc(%ebp),%edx
 33a:	8b 45 08             	mov    0x8(%ebp),%eax
 33d:	01 d0                	add    %edx,%eax
 33f:	c6 00 00             	movb   $0x0,(%eax)
  return buf;
 342:	8b 45 08             	mov    0x8(%ebp),%eax
}
 345:	c9                   	leave  
 346:	c3                   	ret    

00000347 <stat>:

int
stat(const char *n, struct stat *st)
{
 347:	55                   	push   %ebp
 348:	89 e5                	mov    %esp,%ebp
 34a:	83 ec 18             	sub    $0x18,%esp
  int fd;
  int r;

  fd = open(n, O_RDONLY);
 34d:	83 ec 08             	sub    $0x8,%esp
 350:	6a 00                	push   $0x0
 352:	ff 75 08             	push   0x8(%ebp)
 355:	e8 0c 01 00 00       	call   466 <open>
 35a:	83 c4 10             	add    $0x10,%esp
 35d:	89 45 f4             	mov    %eax,-0xc(%ebp)
  if(fd < 0)
 360:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 364:	79 07                	jns    36d <stat+0x26>
    return -1;
 366:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 36b:	eb 25                	jmp    392 <stat+0x4b>
  r = fstat(fd, st);
 36d:	83 ec 08             	sub    $0x8,%esp
 370:	ff 75 0c             	push   0xc(%ebp)
 373:	ff 75 f4             	push   -0xc(%ebp)
 376:	e8 03 01 00 00       	call   47e <fstat>
 37b:	83 c4 10             	add    $0x10,%esp
 37e:	89 45 f0             	mov    %eax,-0x10(%ebp)
  close(fd);
 381:	83 ec 0c             	sub    $0xc,%esp
 384:	ff 75 f4             	push   -0xc(%ebp)
 387:	e8 c2 00 00 00       	call   44e <close>
 38c:	83 c4 10             	add    $0x10,%esp
  return r;
 38f:	8b 45 f0             	mov    -0x10(%ebp),%eax
}
 392:	c9                   	leave  
 393:	c3                   	ret    

00000394 <atoi>:

int
atoi(const char *s)
{
 394:	55                   	push   %ebp
 395:	89 e5                	mov    %esp,%ebp
 397:	83 ec 10             	sub    $0x10,%esp
  int n;

  n = 0;
 39a:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
  while('0' <= *s && *s <= '9')
 3a1:	eb 25                	jmp    3c8 <atoi+0x34>
    n = n*10 + *s++ - '0';
 3a3:	8b 55 fc             	mov    -0x4(%ebp),%edx
 3a6:	89 d0                	mov    %edx,%eax
 3a8:	c1 e0 02             	shl    $0x2,%eax
 3ab:	01 d0                	add    %edx,%eax
 3ad:	01 c0                	add    %eax,%eax
 3af:	89 c1                	mov    %eax,%ecx
 3b1:	8b 45 08             	mov    0x8(%ebp),%eax
 3b4:	8d 50 01             	lea    0x1(%eax),%edx
 3b7:	89 55 08             	mov    %edx,0x8(%ebp)
 3ba:	0f b6 00             	movzbl (%eax),%eax
 3bd:	0f be c0             	movsbl %al,%eax
 3c0:	01 c8                	add    %ecx,%eax
 3c2:	83 e8 30             	sub    $0x30,%eax
 3c5:	89 45 fc             	mov    %eax,-0x4(%ebp)
  while('0' <= *s && *s <= '9')
 3c8:	8b 45 08             	mov    0x8(%ebp),%eax
 3cb:	0f b6 00             	movzbl (%eax),%eax
 3ce:	3c 2f                	cmp    $0x2f,%al
 3d0:	7e 0a                	jle    3dc <atoi+0x48>
 3d2:	8b 45 08             	mov    0x8(%ebp),%eax
 3d5:	0f b6 00             	movzbl (%eax),%eax
 3d8:	3c 39                	cmp    $0x39,%al
 3da:	7e c7                	jle    3a3 <atoi+0xf>
  return n;
 3dc:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 3df:	c9                   	leave  
 3e0:	c3                   	ret    

000003e1 <memmove>:

void*
memmove(void *vdst, const void *vsrc, int n)
{
 3e1:	55                   	push   %ebp
 3e2:	89 e5                	mov    %esp,%ebp
 3e4:	83 ec 10             	sub    $0x10,%esp
  char *dst;
  const char *src;

  dst = vdst;
 3e7:	8b 45 08             	mov    0x8(%ebp),%eax
 3ea:	89 45 fc             	mov    %eax,-0x4(%ebp)
  src = vsrc;
 3ed:	8b 45 0c             	mov    0xc(%ebp),%eax
 3f0:	89 45 f8             	mov    %eax,-0x8(%ebp)
  while(n-- > 0)
 3f3:	eb 17                	jmp    40c <memmove+0x2b>
    *dst++ = *src++;
 3f5:	8b 55 f8             	mov    -0x8(%ebp),%edx
 3f8:	8d 42 01             	lea    0x1(%edx),%eax
 3fb:	89 45 f8             	mov    %eax,-0x8(%ebp)
 3fe:	8b 45 fc             	mov    -0x4(%ebp),%eax
 401:	8d 48 01             	lea    0x1(%eax),%ecx
 404:	89 4d fc             	mov    %ecx,-0x4(%ebp)
 407:	0f b6 12             	movzbl (%edx),%edx
 40a:	88 10                	mov    %dl,(%eax)
  while(n-- > 0)
 40c:	8b 45 10             	mov    0x10(%ebp),%eax
 40f:	8d 50 ff             	lea    -0x1(%eax),%edx
 412:	89 55 10             	mov    %edx,0x10(%ebp)
 415:	85 c0                	test   %eax,%eax
 417:	7f dc                	jg     3f5 <memmove+0x14>
  return vdst;
 419:	8b 45 08             	mov    0x8(%ebp),%eax
}
 41c:	c9                   	leave  
 41d:	c3                   	ret    

0000041e <fork>:
  name: \
    movl $SYS_ ## name, %eax; \
    int $T_SYSCALL; \
    ret

SYSCALL(fork)
 41e:	b8 01 00 00 00       	mov    $0x1,%eax
 423:	cd 40                	int    $0x40
 425:	c3                   	ret    

00000426 <exit>:
SYSCALL(exit)
 426:	b8 02 00 00 00       	mov    $0x2,%eax
 42b:	cd 40                	int    $0x40
 42d:	c3                   	ret    

0000042e <wait>:
SYSCALL(wait)
 42e:	b8 03 00 00 00       	mov    $0x3,%eax
 433:	cd 40                	int    $0x40
 435:	c3                   	ret    

00000436 <pipe>:
SYSCALL(pipe)
 436:	b8 04 00 00 00       	mov    $0x4,%eax
 43b:	cd 40                	int    $0x40
 43d:	c3                   	ret    

0000043e <read>:
SYSCALL(read)
 43e:	b8 05 00 00 00       	mov    $0x5,%eax
 443:	cd 40                	int    $0x40
 445:	c3                   	ret    

00000446 <write>:
SYSCALL(write)
 446:	b8 10 00 00 00       	mov    $0x10,%eax
 44b:	cd 40                	int    $0x40
 44d:	c3                   	ret    

0000044e <close>:
SYSCALL(close)
 44e:	b8 15 00 00 00       	mov    $0x15,%eax
 453:	cd 40                	int    $0x40
 455:	c3                   	ret    

00000456 <kill>:
SYSCALL(kill)
 456:	b8 06 00 00 00       	mov    $0x6,%eax
 45b:	cd 40                	int    $0x40
 45d:	c3                   	ret    

0000045e <exec>:
SYSCALL(exec)
 45e:	b8 07 00 00 00       	mov    $0x7,%eax
 463:	cd 40                	int    $0x40
 465:	c3                   	ret    

00000466 <open>:
SYSCALL(open)
 466:	b8 0f 00 00 00       	mov    $0xf,%eax
 46b:	cd 40                	int    $0x40
 46d:	c3                   	ret    

0000046e <mknod>:
SYSCALL(mknod)
 46e:	b8 11 00 00 00       	mov    $0x11,%eax
 473:	cd 40                	int    $0x40
 475:	c3                   	ret    

00000476 <unlink>:
SYSCALL(unlink)
 476:	b8 12 00 00 00       	mov    $0x12,%eax
 47b:	cd 40                	int    $0x40
 47d:	c3                   	ret    

0000047e <fstat>:
SYSCALL(fstat)
 47e:	b8 08 00 00 00       	mov    $0x8,%eax
 483:	cd 40                	int    $0x40
 485:	c3                   	ret    

00000486 <link>:
SYSCALL(link)
 486:	b8 13 00 00 00       	mov    $0x13,%eax
 48b:	cd 40                	int    $0x40
 48d:	c3                   	ret    

0000048e <mkdir>:
SYSCALL(mkdir)
 48e:	b8 14 00 00 00       	mov    $0x14,%eax
 493:	cd 40                	int    $0x40
 495:	c3                   	ret    

00000496 <chdir>:
SYSCALL(chdir)
 496:	b8 09 00 00 00       	mov    $0x9,%eax
 49b:	cd 40                	int    $0x40
 49d:	c3                   	ret    

0000049e <dup>:
SYSCALL(dup)
 49e:	b8 0a 00 00 00       	mov    $0xa,%eax
 4a3:	cd 40                	int    $0x40
 4a5:	c3                   	ret    

000004a6 <getpid>:
SYSCALL(getpid)
 4a6:	b8 0b 00 00 00       	mov    $0xb,%eax
 4ab:	cd 40                	int    $0x40
 4ad:	c3                   	ret    

000004ae <sbrk>:
SYSCALL(sbrk)
 4ae:	b8 0c 00 00 00       	mov    $0xc,%eax
 4b3:	cd 40                	int    $0x40
 4b5:	c3                   	ret    

000004b6 <sleep>:
SYSCALL(sleep)
 4b6:	b8 0d 00 00 00       	mov    $0xd,%eax
 4bb:	cd 40                	int    $0x40
 4bd:	c3                   	ret    

000004be <uptime>:
SYSCALL(uptime)
 4be:	b8 0e 00 00 00       	mov    $0xe,%eax
 4c3:	cd 40                	int    $0x40
 4c5:	c3                   	ret    

000004c6 <wait2>:
SYSCALL(wait2)
 4c6:	b8 16 00 00 00       	mov    $0x16,%eax
 4cb:	cd 40                	int    $0x40
 4cd:	c3                   	ret    

000004ce <putc>:
#include "stat.h"
#include "user.h"

static void
putc(int fd, char c)
{
 4ce:	55                   	push   %ebp
 4cf:	89 e5                	mov    %esp,%ebp
 4d1:	83 ec 18             	sub    $0x18,%esp
 4d4:	8b 45 0c             	mov    0xc(%ebp),%eax
 4d7:	88 45 f4             	mov    %al,-0xc(%ebp)
  write(fd, &c, 1);
 4da:	83 ec 04             	sub    $0x4,%esp
 4dd:	6a 01                	push   $0x1
 4df:	8d 45 f4             	lea    -0xc(%ebp),%eax
 4e2:	50                   	push   %eax
 4e3:	ff 75 08             	push   0x8(%ebp)
 4e6:	e8 5b ff ff ff       	call   446 <write>
 4eb:	83 c4 10             	add    $0x10,%esp
}
 4ee:	90                   	nop
 4ef:	c9                   	leave  
 4f0:	c3                   	ret    

000004f1 <printint>:

static void
printint(int fd, int xx, int base, int sgn)
{
 4f1:	55                   	push   %ebp
 4f2:	89 e5                	mov    %esp,%ebp
 4f4:	83 ec 28             	sub    $0x28,%esp
  static char digits[] = "0123456789ABCDEF";
  char buf[16];
  int i, neg;
  uint x;

  neg = 0;
 4f7:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
  if(sgn && xx < 0){
 4fe:	83 7d 14 00          	cmpl   $0x0,0x14(%ebp)
 502:	74 17                	je     51b <printint+0x2a>
 504:	83 7d 0c 00          	cmpl   $0x0,0xc(%ebp)
 508:	79 11                	jns    51b <printint+0x2a>
    neg = 1;
 50a:	c7 45 f0 01 00 00 00 	movl   $0x1,-0x10(%ebp)
    x = -xx;
 511:	8b 45 0c             	mov    0xc(%ebp),%eax
 514:	f7 d8                	neg    %eax
 516:	89 45 ec             	mov    %eax,-0x14(%ebp)
 519:	eb 06                	jmp    521 <printint+0x30>
  } else {
    x = xx;
 51b:	8b 45 0c             	mov    0xc(%ebp),%eax
 51e:	89 45 ec             	mov    %eax,-0x14(%ebp)
  }

  i = 0;
 521:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
  do{
    buf[i++] = digits[x % base];
 528:	8b 4d 10             	mov    0x10(%ebp),%ecx
 52b:	8b 45 ec             	mov    -0x14(%ebp),%eax
 52e:	ba 00 00 00 00       	mov    $0x0,%edx
 533:	f7 f1                	div    %ecx
 535:	89 d1                	mov    %edx,%ecx
 537:	8b 45 f4             	mov    -0xc(%ebp),%eax
 53a:	8d 50 01             	lea    0x1(%eax),%edx
 53d:	89 55 f4             	mov    %edx,-0xc(%ebp)
 540:	0f b6 91 ec 0c 00 00 	movzbl 0xcec(%ecx),%edx
 547:	88 54 05 dc          	mov    %dl,-0x24(%ebp,%eax,1)
  }while((x /= base) != 0);
 54b:	8b 4d 10             	mov    0x10(%ebp),%ecx
 54e:	8b 45 ec             	mov    -0x14(%ebp),%eax
 551:	ba 00 00 00 00       	mov    $0x0,%edx
 556:	f7 f1                	div    %ecx
 558:	89 45 ec             	mov    %eax,-0x14(%ebp)
 55b:	83 7d ec 00          	cmpl   $0x0,-0x14(%ebp)
 55f:	75 c7                	jne    528 <printint+0x37>
  if(neg)
 561:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 565:	74 2d                	je     594 <printint+0xa3>
    buf[i++] = '-';
 567:	8b 45 f4             	mov    -0xc(%ebp),%eax
 56a:	8d 50 01             	lea    0x1(%eax),%edx
 56d:	89 55 f4             	mov    %edx,-0xc(%ebp)
 570:	c6 44 05 dc 2d       	movb   $0x2d,-0x24(%ebp,%eax,1)

  while(--i >= 0)
 575:	eb 1d                	jmp    594 <printint+0xa3>
    putc(fd, buf[i]);
 577:	8d 55 dc             	lea    -0x24(%ebp),%edx
 57a:	8b 45 f4             	mov    -0xc(%ebp),%eax
 57d:	01 d0                	add    %edx,%eax
 57f:	0f b6 00             	movzbl (%eax),%eax
 582:	0f be c0             	movsbl %al,%eax
 585:	83 ec 08             	sub    $0x8,%esp
 588:	50                   	push   %eax
 589:	ff 75 08             	push   0x8(%ebp)
 58c:	e8 3d ff ff ff       	call   4ce <putc>
 591:	83 c4 10             	add    $0x10,%esp
  while(--i >= 0)
 594:	83 6d f4 01          	subl   $0x1,-0xc(%ebp)
 598:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 59c:	79 d9                	jns    577 <printint+0x86>
}
 59e:	90                   	nop
 59f:	90                   	nop
 5a0:	c9                   	leave  
 5a1:	c3                   	ret    

000005a2 <printf>:

// Print to the given fd. Only understands %d, %x, %p, %s.
void
printf(int fd, const char *fmt, ...)
{
 5a2:	55                   	push   %ebp
 5a3:	89 e5                	mov    %esp,%ebp
 5a5:	83 ec 28             	sub    $0x28,%esp
  char *s;
  int c, i, state;
  uint *ap;

  state = 0;
 5a8:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
  ap = (uint*)(void*)&fmt + 1;
 5af:	8d 45 0c             	lea    0xc(%ebp),%eax
 5b2:	83 c0 04             	add    $0x4,%eax
 5b5:	89 45 e8             	mov    %eax,-0x18(%ebp)
  for(i = 0; fmt[i]; i++){
 5b8:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
 5bf:	e9 59 01 00 00       	jmp    71d <printf+0x17b>
    c = fmt[i] & 0xff;
 5c4:	8b 55 0c             	mov    0xc(%ebp),%edx
 5c7:	8b 45 f0             	mov    -0x10(%ebp),%eax
 5ca:	01 d0                	add    %edx,%eax
 5cc:	0f b6 00             	movzbl (%eax),%eax
 5cf:	0f be c0             	movsbl %al,%eax
 5d2:	25 ff 00 00 00       	and    $0xff,%eax
 5d7:	89 45 e4             	mov    %eax,-0x1c(%ebp)
    if(state == 0){
 5da:	83 7d ec 00          	cmpl   $0x0,-0x14(%ebp)
 5de:	75 2c                	jne    60c <printf+0x6a>
      if(c == '%'){
 5e0:	83 7d e4 25          	cmpl   $0x25,-0x1c(%ebp)
 5e4:	75 0c                	jne    5f2 <printf+0x50>
        state = '%';
 5e6:	c7 45 ec 25 00 00 00 	movl   $0x25,-0x14(%ebp)
 5ed:	e9 27 01 00 00       	jmp    719 <printf+0x177>
      } else {
        putc(fd, c);
 5f2:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 5f5:	0f be c0             	movsbl %al,%eax
 5f8:	83 ec 08             	sub    $0x8,%esp
 5fb:	50                   	push   %eax
 5fc:	ff 75 08             	push   0x8(%ebp)
 5ff:	e8 ca fe ff ff       	call   4ce <putc>
 604:	83 c4 10             	add    $0x10,%esp
 607:	e9 0d 01 00 00       	jmp    719 <printf+0x177>
      }
    } else if(state == '%'){
 60c:	83 7d ec 25          	cmpl   $0x25,-0x14(%ebp)
 610:	0f 85 03 01 00 00    	jne    719 <printf+0x177>
      if(c == 'd'){
 616:	83 7d e4 64          	cmpl   $0x64,-0x1c(%ebp)
 61a:	75 1e                	jne    63a <printf+0x98>
        printint(fd, *ap, 10, 1);
 61c:	8b 45 e8             	mov    -0x18(%ebp),%eax
 61f:	8b 00                	mov    (%eax),%eax
 621:	6a 01                	push   $0x1
 623:	6a 0a                	push   $0xa
 625:	50                   	push   %eax
 626:	ff 75 08             	push   0x8(%ebp)
 629:	e8 c3 fe ff ff       	call   4f1 <printint>
 62e:	83 c4 10             	add    $0x10,%esp
        ap++;
 631:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 635:	e9 d8 00 00 00       	jmp    712 <printf+0x170>
      } else if(c == 'x' || c == 'p'){
 63a:	83 7d e4 78          	cmpl   $0x78,-0x1c(%ebp)
 63e:	74 06                	je     646 <printf+0xa4>
 640:	83 7d e4 70          	cmpl   $0x70,-0x1c(%ebp)
 644:	75 1e                	jne    664 <printf+0xc2>
        printint(fd, *ap, 16, 0);
 646:	8b 45 e8             	mov    -0x18(%ebp),%eax
 649:	8b 00                	mov    (%eax),%eax
 64b:	6a 00                	push   $0x0
 64d:	6a 10                	push   $0x10
 64f:	50                   	push   %eax
 650:	ff 75 08             	push   0x8(%ebp)
 653:	e8 99 fe ff ff       	call   4f1 <printint>
 658:	83 c4 10             	add    $0x10,%esp
        ap++;
 65b:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 65f:	e9 ae 00 00 00       	jmp    712 <printf+0x170>
      } else if(c == 's'){
 664:	83 7d e4 73          	cmpl   $0x73,-0x1c(%ebp)
 668:	75 43                	jne    6ad <printf+0x10b>
        s = (char*)*ap;
 66a:	8b 45 e8             	mov    -0x18(%ebp),%eax
 66d:	8b 00                	mov    (%eax),%eax
 66f:	89 45 f4             	mov    %eax,-0xc(%ebp)
        ap++;
 672:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
        if(s == 0)
 676:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 67a:	75 25                	jne    6a1 <printf+0xff>
          s = "(null)";
 67c:	c7 45 f4 a0 0a 00 00 	movl   $0xaa0,-0xc(%ebp)
        while(*s != 0){
 683:	eb 1c                	jmp    6a1 <printf+0xff>
          putc(fd, *s);
 685:	8b 45 f4             	mov    -0xc(%ebp),%eax
 688:	0f b6 00             	movzbl (%eax),%eax
 68b:	0f be c0             	movsbl %al,%eax
 68e:	83 ec 08             	sub    $0x8,%esp
 691:	50                   	push   %eax
 692:	ff 75 08             	push   0x8(%ebp)
 695:	e8 34 fe ff ff       	call   4ce <putc>
 69a:	83 c4 10             	add    $0x10,%esp
          s++;
 69d:	83 45 f4 01          	addl   $0x1,-0xc(%ebp)
        while(*s != 0){
 6a1:	8b 45 f4             	mov    -0xc(%ebp),%eax
 6a4:	0f b6 00             	movzbl (%eax),%eax
 6a7:	84 c0                	test   %al,%al
 6a9:	75 da                	jne    685 <printf+0xe3>
 6ab:	eb 65                	jmp    712 <printf+0x170>
        }
      } else if(c == 'c'){
 6ad:	83 7d e4 63          	cmpl   $0x63,-0x1c(%ebp)
 6b1:	75 1d                	jne    6d0 <printf+0x12e>
        putc(fd, *ap);
 6b3:	8b 45 e8             	mov    -0x18(%ebp),%eax
 6b6:	8b 00                	mov    (%eax),%eax
 6b8:	0f be c0             	movsbl %al,%eax
 6bb:	83 ec 08             	sub    $0x8,%esp
 6be:	50                   	push   %eax
 6bf:	ff 75 08             	push   0x8(%ebp)
 6c2:	e8 07 fe ff ff       	call   4ce <putc>
 6c7:	83 c4 10             	add    $0x10,%esp
        ap++;
 6ca:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 6ce:	eb 42                	jmp    712 <printf+0x170>
      } else if(c == '%'){
 6d0:	83 7d e4 25          	cmpl   $0x25,-0x1c(%ebp)
 6d4:	75 17                	jne    6ed <printf+0x14b>
        putc(fd, c);
 6d6:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 6d9:	0f be c0             	movsbl %al,%eax
 6dc:	83 ec 08             	sub    $0x8,%esp
 6df:	50                   	push   %eax
 6e0:	ff 75 08             	push   0x8(%ebp)
 6e3:	e8 e6 fd ff ff       	call   4ce <putc>
 6e8:	83 c4 10             	add    $0x10,%esp
 6eb:	eb 25                	jmp    712 <printf+0x170>
      } else {
        // Unknown % sequence.  Print it to draw attention.
        putc(fd, '%');
 6ed:	83 ec 08             	sub    $0x8,%esp
 6f0:	6a 25                	push   $0x25
 6f2:	ff 75 08             	push   0x8(%ebp)
 6f5:	e8 d4 fd ff ff       	call   4ce <putc>
 6fa:	83 c4 10             	add    $0x10,%esp
        putc(fd, c);
 6fd:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 700:	0f be c0             	movsbl %al,%eax
 703:	83 ec 08             	sub    $0x8,%esp
 706:	50                   	push   %eax
 707:	ff 75 08             	push   0x8(%ebp)
 70a:	e8 bf fd ff ff       	call   4ce <putc>
 70f:	83 c4 10             	add    $0x10,%esp
      }
      state = 0;
 712:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
  for(i = 0; fmt[i]; i++){
 719:	83 45 f0 01          	addl   $0x1,-0x10(%ebp)
 71d:	8b 55 0c             	mov    0xc(%ebp),%edx
 720:	8b 45 f0             	mov    -0x10(%ebp),%eax
 723:	01 d0                	add    %edx,%eax
 725:	0f b6 00             	movzbl (%eax),%eax
 728:	84 c0                	test   %al,%al
 72a:	0f 85 94 fe ff ff    	jne    5c4 <printf+0x22>
    }
  }
}
 730:	90                   	nop
 731:	90                   	nop
 732:	c9                   	leave  
 733:	c3                   	ret    

00000734 <free>:
static Header base;
static Header *freep;

void
free(void *ap)
{
 734:	55                   	push   %ebp
 735:	89 e5                	mov    %esp,%ebp
 737:	83 ec 10             	sub    $0x10,%esp
  Header *bp, *p;

  bp = (Header*)ap - 1;
 73a:	8b 45 08             	mov    0x8(%ebp),%eax
 73d:	83 e8 08             	sub    $0x8,%eax
 740:	89 45 f8             	mov    %eax,-0x8(%ebp)
  for(p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
 743:	a1 08 0d 00 00       	mov    0xd08,%eax
 748:	89 45 fc             	mov    %eax,-0x4(%ebp)
 74b:	eb 24                	jmp    771 <free+0x3d>
    if(p >= p->s.ptr && (bp > p || bp < p->s.ptr))
 74d:	8b 45 fc             	mov    -0x4(%ebp),%eax
 750:	8b 00                	mov    (%eax),%eax
 752:	39 45 fc             	cmp    %eax,-0x4(%ebp)
 755:	72 12                	jb     769 <free+0x35>
 757:	8b 45 f8             	mov    -0x8(%ebp),%eax
 75a:	3b 45 fc             	cmp    -0x4(%ebp),%eax
 75d:	77 24                	ja     783 <free+0x4f>
 75f:	8b 45 fc             	mov    -0x4(%ebp),%eax
 762:	8b 00                	mov    (%eax),%eax
 764:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 767:	72 1a                	jb     783 <free+0x4f>
  for(p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
 769:	8b 45 fc             	mov    -0x4(%ebp),%eax
 76c:	8b 00                	mov    (%eax),%eax
 76e:	89 45 fc             	mov    %eax,-0x4(%ebp)
 771:	8b 45 f8             	mov    -0x8(%ebp),%eax
 774:	3b 45 fc             	cmp    -0x4(%ebp),%eax
 777:	76 d4                	jbe    74d <free+0x19>
 779:	8b 45 fc             	mov    -0x4(%ebp),%eax
 77c:	8b 00                	mov    (%eax),%eax
 77e:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 781:	73 ca                	jae    74d <free+0x19>
      break;
  if(bp + bp->s.size == p->s.ptr){
 783:	8b 45 f8             	mov    -0x8(%ebp),%eax
 786:	8b 40 04             	mov    0x4(%eax),%eax
 789:	8d 14 c5 00 00 00 00 	lea    0x0(,%eax,8),%edx
 790:	8b 45 f8             	mov    -0x8(%ebp),%eax
 793:	01 c2                	add    %eax,%edx
 795:	8b 45 fc             	mov    -0x4(%ebp),%eax
 798:	8b 00                	mov    (%eax),%eax
 79a:	39 c2                	cmp    %eax,%edx
 79c:	75 24                	jne    7c2 <free+0x8e>
    bp->s.size += p->s.ptr->s.size;
 79e:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7a1:	8b 50 04             	mov    0x4(%eax),%edx
 7a4:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7a7:	8b 00                	mov    (%eax),%eax
 7a9:	8b 40 04             	mov    0x4(%eax),%eax
 7ac:	01 c2                	add    %eax,%edx
 7ae:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7b1:	89 50 04             	mov    %edx,0x4(%eax)
    bp->s.ptr = p->s.ptr->s.ptr;
 7b4:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7b7:	8b 00                	mov    (%eax),%eax
 7b9:	8b 10                	mov    (%eax),%edx
 7bb:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7be:	89 10                	mov    %edx,(%eax)
 7c0:	eb 0a                	jmp    7cc <free+0x98>
  } else
    bp->s.ptr = p->s.ptr;
 7c2:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7c5:	8b 10                	mov    (%eax),%edx
 7c7:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7ca:	89 10                	mov    %edx,(%eax)
  if(p + p->s.size == bp){
 7cc:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7cf:	8b 40 04             	mov    0x4(%eax),%eax
 7d2:	8d 14 c5 00 00 00 00 	lea    0x0(,%eax,8),%edx
 7d9:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7dc:	01 d0                	add    %edx,%eax
 7de:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 7e1:	75 20                	jne    803 <free+0xcf>
    p->s.size += bp->s.size;
 7e3:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7e6:	8b 50 04             	mov    0x4(%eax),%edx
 7e9:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7ec:	8b 40 04             	mov    0x4(%eax),%eax
 7ef:	01 c2                	add    %eax,%edx
 7f1:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7f4:	89 50 04             	mov    %edx,0x4(%eax)
    p->s.ptr = bp->s.ptr;
 7f7:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7fa:	8b 10                	mov    (%eax),%edx
 7fc:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7ff:	89 10                	mov    %edx,(%eax)
 801:	eb 08                	jmp    80b <free+0xd7>
  } else
    p->s.ptr = bp;
 803:	8b 45 fc             	mov    -0x4(%ebp),%eax
 806:	8b 55 f8             	mov    -0x8(%ebp),%edx
 809:	89 10                	mov    %edx,(%eax)
  freep = p;
 80b:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80e:	a3 08 0d 00 00       	mov    %eax,0xd08
}
 813:	90                   	nop
 814:	c9                   	leave  
 815:	c3                   	ret    

00000816 <morecore>:

static Header*
morecore(uint nu)
{
 816:	55                   	push   %ebp
 817:	89 e5                	mov    %esp,%ebp
 819:	83 ec 18             	sub    $0x18,%esp
  char *p;
  Header *hp;

  if(nu < 4096)
 81c:	81 7d 08 ff 0f 00 00 	cmpl   $0xfff,0x8(%ebp)
 823:	77 07                	ja     82c <morecore+0x16>
    nu = 4096;
 825:	c7 45 08 00 10 00 00 	movl   $0x1000,0x8(%ebp)
  p = sbrk(nu * sizeof(Header));
 82c:	8b 45 08             	mov    0x8(%ebp),%eax
 82f:	c1 e0 03             	shl    $0x3,%eax
 832:	83 ec 0c             	sub    $0xc,%esp
 835:	50                   	push   %eax
 836:	e8 73 fc ff ff       	call   4ae <sbrk>
 83b:	83 c4 10             	add    $0x10,%esp
 83e:	89 45 f4             	mov    %eax,-0xc(%ebp)
  if(p == (char*)-1)
 841:	83 7d f4 ff          	cmpl   $0xffffffff,-0xc(%ebp)
 845:	75 07                	jne    84e <morecore+0x38>
    return 0;
 847:	b8 00 00 00 00       	mov    $0x0,%eax
 84c:	eb 26                	jmp    874 <morecore+0x5e>
  hp = (Header*)p;
 84e:	8b 45 f4             	mov    -0xc(%ebp),%eax
 851:	89 45 f0             	mov    %eax,-0x10(%ebp)
  hp->s.size = nu;
 854:	8b 45 f0             	mov    -0x10(%ebp),%eax
 857:	8b 55 08             	mov    0x8(%ebp),%edx
 85a:	89 50 04             	mov    %edx,0x4(%eax)
  free((void*)(hp + 1));
 85d:	8b 45 f0             	mov    -0x10(%ebp),%eax
 860:	83 c0 08             	add    $0x8,%eax
 863:	83 ec 0c             	sub    $0xc,%esp
 866:	50                   	push   %eax
 867:	e8 c8 fe ff ff       	call   734 <free>
 86c:	83 c4 10             	add    $0x10,%esp
  return freep;
 86f:	a1 08 0d 00 00       	mov    0xd08,%eax
}
 874:	c9                   	leave  
 875:	c3                   	ret    

00000876 <malloc>:

void*
malloc(uint nbytes)
{
 876:	55                   	push   %ebp
 877:	89 e5                	mov    %esp,%ebp
 879:	83 ec 18             	sub    $0x18,%esp
  Header *p, *prevp;
  uint nunits;

  nunits = (nbytes + sizeof(Header) - 1)/sizeof(Header) + 1;
 87c:	8b 45 08             	mov    0x8(%ebp),%eax
 87f:	83 c0 07             	add    $0x7,%eax
 882:	c1 e8 03             	shr    $0x3,%eax
 885:	83 c0 01             	add    $0x1,%eax
 888:	89 45 ec             	mov    %eax,-0x14(%ebp)
  if((prevp = freep) == 0){
 88b:	a1 08 0d 00 00       	mov    0xd08,%eax
 890:	89 45 f0             	mov    %eax,-0x10(%ebp)
 893:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 897:	75 23                	jne    8bc <malloc+0x46>
    base.s.ptr = freep = prevp = &base;
 899:	c7 45 f0 00 0d 00 00 	movl   $0xd00,-0x10(%ebp)
 8a0:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8a3:	a3 08 0d 00 00       	mov    %eax,0xd08
 8a8:	a1 08 0d 00 00       	mov    0xd08,%eax
 8ad:	a3 00 0d 00 00       	mov    %eax,0xd00
    base.s.size = 0;
 8b2:	c7 05 04 0d 00 00 00 	movl   $0x0,0xd04
 8b9:	00 00 00 
  }
  for(p = prevp->s.ptr; ; prevp = p, p = p->s.ptr){
 8bc:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8bf:	8b 00                	mov    (%eax),%eax
 8c1:	89 45 f4             	mov    %eax,-0xc(%ebp)
    if(p->s.size >= nunits){
 8c4:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8c7:	8b 40 04             	mov    0x4(%eax),%eax
 8ca:	39 45 ec             	cmp    %eax,-0x14(%ebp)
 8cd:	77 4d                	ja     91c <malloc+0xa6>
      if(p->s.size == nunits)
 8cf:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8d2:	8b 40 04             	mov    0x4(%eax),%eax
 8d5:	39 45 ec             	cmp    %eax,-0x14(%ebp)
 8d8:	75 0c                	jne    8e6 <malloc+0x70>
        prevp->s.ptr = p->s.ptr;
 8da:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8dd:	8b 10                	mov    (%eax),%edx
 8df:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8e2:	89 10                	mov    %edx,(%eax)
 8e4:	eb 26                	jmp    90c <malloc+0x96>
      else {
        p->s.size -= nunits;
 8e6:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8e9:	8b 40 04             	mov    0x4(%eax),%eax
 8ec:	2b 45 ec             	sub    -0x14(%ebp),%eax
 8ef:	89 c2                	mov    %eax,%edx
 8f1:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8f4:	89 50 04             	mov    %edx,0x4(%eax)
        p += p->s.size;
 8f7:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8fa:	8b 40 04             	mov    0x4(%eax),%eax
 8fd:	c1 e0 03             	shl    $0x3,%eax
 900:	01 45 f4             	add    %eax,-0xc(%ebp)
        p->s.size = nunits;
 903:	8b 45 f4             	mov    -0xc(%ebp),%eax
 906:	8b 55 ec             	mov    -0x14(%ebp),%edx
 909:	89 50 04             	mov    %edx,0x4(%eax)
      }
      freep = prevp;
 90c:	8b 45 f0             	mov    -0x10(%ebp),%eax
 90f:	a3 08 0d 00 00       	mov    %eax,0xd08
      return (void*)(p + 1);
 914:	8b 45 f4             	mov    -0xc(%ebp),%eax
 917:	83 c0 08             	add    $0x8,%eax
 91a:	eb 3b                	jmp    957 <malloc+0xe1>
    }
    if(p == freep)
 91c:	a1 08 0d 00 00       	mov    0xd08,%eax
 921:	39 45 f4             	cmp    %eax,-0xc(%ebp)
 924:	75 1e                	jne    944 <malloc+0xce>
      if((p = morecore(nunits)) == 0)
 926:	83 ec 0c             	sub    $0xc,%esp
 929:	ff 75 ec             	push   -0x14(%ebp)
 92c:	e8 e5 fe ff ff       	call   816 <morecore>
 931:	83 c4 10             	add    $0x10,%esp
 934:	89 45 f4             	mov    %eax,-0xc(%ebp)
 937:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 93b:	75 07                	jne    944 <malloc+0xce>
        return 0;
 93d:	b8 00 00 00 00       	mov    $0x0,%eax
 942:	eb 13                	jmp    957 <malloc+0xe1>
  for(p = prevp->s.ptr; ; prevp = p, p = p->s.ptr){
 944:	8b 45 f4             	mov    -0xc(%ebp),%eax
 947:	89 45 f0             	mov    %eax,-0x10(%ebp)
 94a:	8b 45 f4             	mov    -0xc(%ebp),%eax
 94d:	8b 00                	mov    (%eax),%eax
 94f:	89 45 f4             	mov    %eax,-0xc(%ebp)
    if(p->s.size >= nunits){
 952:	e9 6d ff ff ff       	jmp    8c4 <malloc+0x4e>
  }
}
 957:	c9                   	leave  
 958:	c3                   	ret    
