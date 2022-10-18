
_test2:     file format elf32-i386


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
  3f:	e8 65 05 00 00       	call   5a9 <printf>
  44:	83 c4 10             	add    $0x10,%esp
    int wtime1, rtime1;
    int status = wait2(&wtime1, &rtime1);
  47:	83 ec 08             	sub    $0x8,%esp
  4a:	8d 45 dc             	lea    -0x24(%ebp),%eax
  4d:	50                   	push   %eax
  4e:	8d 45 e0             	lea    -0x20(%ebp),%eax
  51:	50                   	push   %eax
  52:	e8 76 04 00 00       	call   4cd <wait2>
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
  70:	e8 34 05 00 00       	call   5a9 <printf>
  75:	83 c4 10             	add    $0x10,%esp
  78:	eb 12                	jmp    8c <main+0x8c>
    } else {
        printf(1, "wait2 should return -1 if calling process has no children\n");
  7a:	83 ec 08             	sub    $0x8,%esp
  7d:	68 94 09 00 00       	push   $0x994
  82:	6a 01                	push   $0x1
  84:	e8 20 05 00 00       	call   5a9 <printf>
  89:	83 c4 10             	add    $0x10,%esp
    }


    printf(1, "*Case2: Parent has children*\n");
  8c:	83 ec 08             	sub    $0x8,%esp
  8f:	68 cf 09 00 00       	push   $0x9cf
  94:	6a 01                	push   $0x1
  96:	e8 0e 05 00 00       	call   5a9 <printf>
  9b:	83 c4 10             	add    $0x10,%esp
    for ( int child = 0; child < NCHILD; child++ ) {
  9e:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
  a5:	e9 cd 00 00 00       	jmp    177 <main+0x177>
        int pid = fork ();
  aa:	e8 76 03 00 00       	call   425 <fork>
  af:	89 45 e4             	mov    %eax,-0x1c(%ebp)
        if ( pid < 0 ) {
  b2:	83 7d e4 00          	cmpl   $0x0,-0x1c(%ebp)
  b6:	79 1d                	jns    d5 <main+0xd5>
            printf(1, "%d failed in fork!\n", getpid());
  b8:	e8 f0 03 00 00       	call   4ad <getpid>
  bd:	83 ec 04             	sub    $0x4,%esp
  c0:	50                   	push   %eax
  c1:	68 ed 09 00 00       	push   $0x9ed
  c6:	6a 01                	push   $0x1
  c8:	e8 dc 04 00 00       	call   5a9 <printf>
  cd:	83 c4 10             	add    $0x10,%esp
            exit();
  d0:	e8 58 03 00 00       	call   42d <exit>
        } else if (pid == 0) {
  d5:	83 7d e4 00          	cmpl   $0x0,-0x1c(%ebp)
  d9:	0f 85 94 00 00 00    	jne    173 <main+0x173>
            sleep(100);
  df:	83 ec 0c             	sub    $0xc,%esp
  e2:	6a 64                	push   $0x64
  e4:	e8 d4 03 00 00       	call   4bd <sleep>
  e9:	83 c4 10             	add    $0x10,%esp
            printf(1, "Child %d created\n",getpid());
  ec:	e8 bc 03 00 00       	call   4ad <getpid>
  f1:	83 ec 04             	sub    $0x4,%esp
  f4:	50                   	push   %eax
  f5:	68 01 0a 00 00       	push   $0xa01
  fa:	6a 01                	push   $0x1
  fc:	e8 a8 04 00 00       	call   5a9 <printf>
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
            for (z = 0; z < child * 90000.0; z += 0.1)
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
            for (z = 0; z < child * 90000.0; z += 0.1)
 132:	dd 45 b0             	fldl   -0x50(%ebp)
 135:	dd 05 90 0a 00 00    	fldl   0xa90
 13b:	de c1                	faddp  %st,%st(1)
 13d:	dd 5d b0             	fstpl  -0x50(%ebp)
 140:	db 45 f0             	fildl  -0x10(%ebp)
 143:	dd 05 98 0a 00 00    	fldl   0xa98
 149:	de c9                	fmulp  %st,%st(1)
 14b:	dd 45 b0             	fldl   -0x50(%ebp)
 14e:	d9 c9                	fxch   %st(1)
 150:	df f1                	fcomip %st(1),%st
 152:	dd d8                	fstp   %st(0)
 154:	77 cc                	ja     122 <main+0x122>
            }
            printf(1, "Child %d finished\n",getpid());
 156:	e8 52 03 00 00       	call   4ad <getpid>
 15b:	83 ec 04             	sub    $0x4,%esp
 15e:	50                   	push   %eax
 15f:	68 13 0a 00 00       	push   $0xa13
 164:	6a 01                	push   $0x1
 166:	e8 3e 04 00 00       	call   5a9 <printf>
 16b:	83 c4 10             	add    $0x10,%esp
            exit();
 16e:	e8 ba 02 00 00       	call   42d <exit>
    for ( int child = 0; child < NCHILD; child++ ) {
 173:	83 45 f0 01          	addl   $0x1,-0x10(%ebp)
 177:	8b 45 f0             	mov    -0x10(%ebp),%eax
 17a:	3b 45 f4             	cmp    -0xc(%ebp),%eax
 17d:	0f 8c 27 ff ff ff    	jl     aa <main+0xaa>
        }
    }
    int wtime, rtime;
    for(int i=0; i<NCHILD; i++){
 183:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
 18a:	eb 3d                	jmp    1c9 <main+0x1c9>
        status = wait2(&wtime, &rtime);
 18c:	83 ec 08             	sub    $0x8,%esp
 18f:	8d 45 d4             	lea    -0x2c(%ebp),%eax
 192:	50                   	push   %eax
 193:	8d 45 d8             	lea    -0x28(%ebp),%eax
 196:	50                   	push   %eax
 197:	e8 31 03 00 00       	call   4cd <wait2>
 19c:	83 c4 10             	add    $0x10,%esp
 19f:	89 45 e8             	mov    %eax,-0x18(%ebp)
        printf(1, "Child no. %d, Child pid: %d exited with Status: %d, Waiting Time: %d, Run Time: %d\n", i, status, status, wtime, rtime);
 1a2:	8b 55 d4             	mov    -0x2c(%ebp),%edx
 1a5:	8b 45 d8             	mov    -0x28(%ebp),%eax
 1a8:	83 ec 04             	sub    $0x4,%esp
 1ab:	52                   	push   %edx
 1ac:	50                   	push   %eax
 1ad:	ff 75 e8             	push   -0x18(%ebp)
 1b0:	ff 75 e8             	push   -0x18(%ebp)
 1b3:	ff 75 ec             	push   -0x14(%ebp)
 1b6:	68 28 0a 00 00       	push   $0xa28
 1bb:	6a 01                	push   $0x1
 1bd:	e8 e7 03 00 00       	call   5a9 <printf>
 1c2:	83 c4 20             	add    $0x20,%esp
    for(int i=0; i<NCHILD; i++){
 1c5:	83 45 ec 01          	addl   $0x1,-0x14(%ebp)
 1c9:	8b 45 ec             	mov    -0x14(%ebp),%eax
 1cc:	3b 45 f4             	cmp    -0xc(%ebp),%eax
 1cf:	7c bb                	jl     18c <main+0x18c>
    }
    exit();
 1d1:	e8 57 02 00 00       	call   42d <exit>

000001d6 <stosb>:
               "cc");
}

static inline void
stosb(void *addr, int data, int cnt)
{
 1d6:	55                   	push   %ebp
 1d7:	89 e5                	mov    %esp,%ebp
 1d9:	57                   	push   %edi
 1da:	53                   	push   %ebx
  asm volatile("cld; rep stosb" :
 1db:	8b 4d 08             	mov    0x8(%ebp),%ecx
 1de:	8b 55 10             	mov    0x10(%ebp),%edx
 1e1:	8b 45 0c             	mov    0xc(%ebp),%eax
 1e4:	89 cb                	mov    %ecx,%ebx
 1e6:	89 df                	mov    %ebx,%edi
 1e8:	89 d1                	mov    %edx,%ecx
 1ea:	fc                   	cld    
 1eb:	f3 aa                	rep stos %al,%es:(%edi)
 1ed:	89 ca                	mov    %ecx,%edx
 1ef:	89 fb                	mov    %edi,%ebx
 1f1:	89 5d 08             	mov    %ebx,0x8(%ebp)
 1f4:	89 55 10             	mov    %edx,0x10(%ebp)
               "=D" (addr), "=c" (cnt) :
               "0" (addr), "1" (cnt), "a" (data) :
               "memory", "cc");
}
 1f7:	90                   	nop
 1f8:	5b                   	pop    %ebx
 1f9:	5f                   	pop    %edi
 1fa:	5d                   	pop    %ebp
 1fb:	c3                   	ret    

000001fc <strcpy>:
#include "user.h"
#include "x86.h"

char*
strcpy(char *s, const char *t)
{
 1fc:	55                   	push   %ebp
 1fd:	89 e5                	mov    %esp,%ebp
 1ff:	83 ec 10             	sub    $0x10,%esp
  char *os;

  os = s;
 202:	8b 45 08             	mov    0x8(%ebp),%eax
 205:	89 45 fc             	mov    %eax,-0x4(%ebp)
  while((*s++ = *t++) != 0)
 208:	90                   	nop
 209:	8b 55 0c             	mov    0xc(%ebp),%edx
 20c:	8d 42 01             	lea    0x1(%edx),%eax
 20f:	89 45 0c             	mov    %eax,0xc(%ebp)
 212:	8b 45 08             	mov    0x8(%ebp),%eax
 215:	8d 48 01             	lea    0x1(%eax),%ecx
 218:	89 4d 08             	mov    %ecx,0x8(%ebp)
 21b:	0f b6 12             	movzbl (%edx),%edx
 21e:	88 10                	mov    %dl,(%eax)
 220:	0f b6 00             	movzbl (%eax),%eax
 223:	84 c0                	test   %al,%al
 225:	75 e2                	jne    209 <strcpy+0xd>
    ;
  return os;
 227:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 22a:	c9                   	leave  
 22b:	c3                   	ret    

0000022c <strcmp>:

int
strcmp(const char *p, const char *q)
{
 22c:	55                   	push   %ebp
 22d:	89 e5                	mov    %esp,%ebp
  while(*p && *p == *q)
 22f:	eb 08                	jmp    239 <strcmp+0xd>
    p++, q++;
 231:	83 45 08 01          	addl   $0x1,0x8(%ebp)
 235:	83 45 0c 01          	addl   $0x1,0xc(%ebp)
  while(*p && *p == *q)
 239:	8b 45 08             	mov    0x8(%ebp),%eax
 23c:	0f b6 00             	movzbl (%eax),%eax
 23f:	84 c0                	test   %al,%al
 241:	74 10                	je     253 <strcmp+0x27>
 243:	8b 45 08             	mov    0x8(%ebp),%eax
 246:	0f b6 10             	movzbl (%eax),%edx
 249:	8b 45 0c             	mov    0xc(%ebp),%eax
 24c:	0f b6 00             	movzbl (%eax),%eax
 24f:	38 c2                	cmp    %al,%dl
 251:	74 de                	je     231 <strcmp+0x5>
  return (uchar)*p - (uchar)*q;
 253:	8b 45 08             	mov    0x8(%ebp),%eax
 256:	0f b6 00             	movzbl (%eax),%eax
 259:	0f b6 d0             	movzbl %al,%edx
 25c:	8b 45 0c             	mov    0xc(%ebp),%eax
 25f:	0f b6 00             	movzbl (%eax),%eax
 262:	0f b6 c8             	movzbl %al,%ecx
 265:	89 d0                	mov    %edx,%eax
 267:	29 c8                	sub    %ecx,%eax
}
 269:	5d                   	pop    %ebp
 26a:	c3                   	ret    

0000026b <strlen>:

uint
strlen(const char *s)
{
 26b:	55                   	push   %ebp
 26c:	89 e5                	mov    %esp,%ebp
 26e:	83 ec 10             	sub    $0x10,%esp
  int n;

  for(n = 0; s[n]; n++)
 271:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
 278:	eb 04                	jmp    27e <strlen+0x13>
 27a:	83 45 fc 01          	addl   $0x1,-0x4(%ebp)
 27e:	8b 55 fc             	mov    -0x4(%ebp),%edx
 281:	8b 45 08             	mov    0x8(%ebp),%eax
 284:	01 d0                	add    %edx,%eax
 286:	0f b6 00             	movzbl (%eax),%eax
 289:	84 c0                	test   %al,%al
 28b:	75 ed                	jne    27a <strlen+0xf>
    ;
  return n;
 28d:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 290:	c9                   	leave  
 291:	c3                   	ret    

00000292 <memset>:

void*
memset(void *dst, int c, uint n)
{
 292:	55                   	push   %ebp
 293:	89 e5                	mov    %esp,%ebp
  stosb(dst, c, n);
 295:	8b 45 10             	mov    0x10(%ebp),%eax
 298:	50                   	push   %eax
 299:	ff 75 0c             	push   0xc(%ebp)
 29c:	ff 75 08             	push   0x8(%ebp)
 29f:	e8 32 ff ff ff       	call   1d6 <stosb>
 2a4:	83 c4 0c             	add    $0xc,%esp
  return dst;
 2a7:	8b 45 08             	mov    0x8(%ebp),%eax
}
 2aa:	c9                   	leave  
 2ab:	c3                   	ret    

000002ac <strchr>:

char*
strchr(const char *s, char c)
{
 2ac:	55                   	push   %ebp
 2ad:	89 e5                	mov    %esp,%ebp
 2af:	83 ec 04             	sub    $0x4,%esp
 2b2:	8b 45 0c             	mov    0xc(%ebp),%eax
 2b5:	88 45 fc             	mov    %al,-0x4(%ebp)
  for(; *s; s++)
 2b8:	eb 14                	jmp    2ce <strchr+0x22>
    if(*s == c)
 2ba:	8b 45 08             	mov    0x8(%ebp),%eax
 2bd:	0f b6 00             	movzbl (%eax),%eax
 2c0:	38 45 fc             	cmp    %al,-0x4(%ebp)
 2c3:	75 05                	jne    2ca <strchr+0x1e>
      return (char*)s;
 2c5:	8b 45 08             	mov    0x8(%ebp),%eax
 2c8:	eb 13                	jmp    2dd <strchr+0x31>
  for(; *s; s++)
 2ca:	83 45 08 01          	addl   $0x1,0x8(%ebp)
 2ce:	8b 45 08             	mov    0x8(%ebp),%eax
 2d1:	0f b6 00             	movzbl (%eax),%eax
 2d4:	84 c0                	test   %al,%al
 2d6:	75 e2                	jne    2ba <strchr+0xe>
  return 0;
 2d8:	b8 00 00 00 00       	mov    $0x0,%eax
}
 2dd:	c9                   	leave  
 2de:	c3                   	ret    

000002df <gets>:

char*
gets(char *buf, int max)
{
 2df:	55                   	push   %ebp
 2e0:	89 e5                	mov    %esp,%ebp
 2e2:	83 ec 18             	sub    $0x18,%esp
  int i, cc;
  char c;

  for(i=0; i+1 < max; ){
 2e5:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
 2ec:	eb 42                	jmp    330 <gets+0x51>
    cc = read(0, &c, 1);
 2ee:	83 ec 04             	sub    $0x4,%esp
 2f1:	6a 01                	push   $0x1
 2f3:	8d 45 ef             	lea    -0x11(%ebp),%eax
 2f6:	50                   	push   %eax
 2f7:	6a 00                	push   $0x0
 2f9:	e8 47 01 00 00       	call   445 <read>
 2fe:	83 c4 10             	add    $0x10,%esp
 301:	89 45 f0             	mov    %eax,-0x10(%ebp)
    if(cc < 1)
 304:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 308:	7e 33                	jle    33d <gets+0x5e>
      break;
    buf[i++] = c;
 30a:	8b 45 f4             	mov    -0xc(%ebp),%eax
 30d:	8d 50 01             	lea    0x1(%eax),%edx
 310:	89 55 f4             	mov    %edx,-0xc(%ebp)
 313:	89 c2                	mov    %eax,%edx
 315:	8b 45 08             	mov    0x8(%ebp),%eax
 318:	01 c2                	add    %eax,%edx
 31a:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 31e:	88 02                	mov    %al,(%edx)
    if(c == '\n' || c == '\r')
 320:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 324:	3c 0a                	cmp    $0xa,%al
 326:	74 16                	je     33e <gets+0x5f>
 328:	0f b6 45 ef          	movzbl -0x11(%ebp),%eax
 32c:	3c 0d                	cmp    $0xd,%al
 32e:	74 0e                	je     33e <gets+0x5f>
  for(i=0; i+1 < max; ){
 330:	8b 45 f4             	mov    -0xc(%ebp),%eax
 333:	83 c0 01             	add    $0x1,%eax
 336:	39 45 0c             	cmp    %eax,0xc(%ebp)
 339:	7f b3                	jg     2ee <gets+0xf>
 33b:	eb 01                	jmp    33e <gets+0x5f>
      break;
 33d:	90                   	nop
      break;
  }
  buf[i] = '\0';
 33e:	8b 55 f4             	mov    -0xc(%ebp),%edx
 341:	8b 45 08             	mov    0x8(%ebp),%eax
 344:	01 d0                	add    %edx,%eax
 346:	c6 00 00             	movb   $0x0,(%eax)
  return buf;
 349:	8b 45 08             	mov    0x8(%ebp),%eax
}
 34c:	c9                   	leave  
 34d:	c3                   	ret    

0000034e <stat>:

int
stat(const char *n, struct stat *st)
{
 34e:	55                   	push   %ebp
 34f:	89 e5                	mov    %esp,%ebp
 351:	83 ec 18             	sub    $0x18,%esp
  int fd;
  int r;

  fd = open(n, O_RDONLY);
 354:	83 ec 08             	sub    $0x8,%esp
 357:	6a 00                	push   $0x0
 359:	ff 75 08             	push   0x8(%ebp)
 35c:	e8 0c 01 00 00       	call   46d <open>
 361:	83 c4 10             	add    $0x10,%esp
 364:	89 45 f4             	mov    %eax,-0xc(%ebp)
  if(fd < 0)
 367:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 36b:	79 07                	jns    374 <stat+0x26>
    return -1;
 36d:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 372:	eb 25                	jmp    399 <stat+0x4b>
  r = fstat(fd, st);
 374:	83 ec 08             	sub    $0x8,%esp
 377:	ff 75 0c             	push   0xc(%ebp)
 37a:	ff 75 f4             	push   -0xc(%ebp)
 37d:	e8 03 01 00 00       	call   485 <fstat>
 382:	83 c4 10             	add    $0x10,%esp
 385:	89 45 f0             	mov    %eax,-0x10(%ebp)
  close(fd);
 388:	83 ec 0c             	sub    $0xc,%esp
 38b:	ff 75 f4             	push   -0xc(%ebp)
 38e:	e8 c2 00 00 00       	call   455 <close>
 393:	83 c4 10             	add    $0x10,%esp
  return r;
 396:	8b 45 f0             	mov    -0x10(%ebp),%eax
}
 399:	c9                   	leave  
 39a:	c3                   	ret    

0000039b <atoi>:

int
atoi(const char *s)
{
 39b:	55                   	push   %ebp
 39c:	89 e5                	mov    %esp,%ebp
 39e:	83 ec 10             	sub    $0x10,%esp
  int n;

  n = 0;
 3a1:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%ebp)
  while('0' <= *s && *s <= '9')
 3a8:	eb 25                	jmp    3cf <atoi+0x34>
    n = n*10 + *s++ - '0';
 3aa:	8b 55 fc             	mov    -0x4(%ebp),%edx
 3ad:	89 d0                	mov    %edx,%eax
 3af:	c1 e0 02             	shl    $0x2,%eax
 3b2:	01 d0                	add    %edx,%eax
 3b4:	01 c0                	add    %eax,%eax
 3b6:	89 c1                	mov    %eax,%ecx
 3b8:	8b 45 08             	mov    0x8(%ebp),%eax
 3bb:	8d 50 01             	lea    0x1(%eax),%edx
 3be:	89 55 08             	mov    %edx,0x8(%ebp)
 3c1:	0f b6 00             	movzbl (%eax),%eax
 3c4:	0f be c0             	movsbl %al,%eax
 3c7:	01 c8                	add    %ecx,%eax
 3c9:	83 e8 30             	sub    $0x30,%eax
 3cc:	89 45 fc             	mov    %eax,-0x4(%ebp)
  while('0' <= *s && *s <= '9')
 3cf:	8b 45 08             	mov    0x8(%ebp),%eax
 3d2:	0f b6 00             	movzbl (%eax),%eax
 3d5:	3c 2f                	cmp    $0x2f,%al
 3d7:	7e 0a                	jle    3e3 <atoi+0x48>
 3d9:	8b 45 08             	mov    0x8(%ebp),%eax
 3dc:	0f b6 00             	movzbl (%eax),%eax
 3df:	3c 39                	cmp    $0x39,%al
 3e1:	7e c7                	jle    3aa <atoi+0xf>
  return n;
 3e3:	8b 45 fc             	mov    -0x4(%ebp),%eax
}
 3e6:	c9                   	leave  
 3e7:	c3                   	ret    

000003e8 <memmove>:

void*
memmove(void *vdst, const void *vsrc, int n)
{
 3e8:	55                   	push   %ebp
 3e9:	89 e5                	mov    %esp,%ebp
 3eb:	83 ec 10             	sub    $0x10,%esp
  char *dst;
  const char *src;

  dst = vdst;
 3ee:	8b 45 08             	mov    0x8(%ebp),%eax
 3f1:	89 45 fc             	mov    %eax,-0x4(%ebp)
  src = vsrc;
 3f4:	8b 45 0c             	mov    0xc(%ebp),%eax
 3f7:	89 45 f8             	mov    %eax,-0x8(%ebp)
  while(n-- > 0)
 3fa:	eb 17                	jmp    413 <memmove+0x2b>
    *dst++ = *src++;
 3fc:	8b 55 f8             	mov    -0x8(%ebp),%edx
 3ff:	8d 42 01             	lea    0x1(%edx),%eax
 402:	89 45 f8             	mov    %eax,-0x8(%ebp)
 405:	8b 45 fc             	mov    -0x4(%ebp),%eax
 408:	8d 48 01             	lea    0x1(%eax),%ecx
 40b:	89 4d fc             	mov    %ecx,-0x4(%ebp)
 40e:	0f b6 12             	movzbl (%edx),%edx
 411:	88 10                	mov    %dl,(%eax)
  while(n-- > 0)
 413:	8b 45 10             	mov    0x10(%ebp),%eax
 416:	8d 50 ff             	lea    -0x1(%eax),%edx
 419:	89 55 10             	mov    %edx,0x10(%ebp)
 41c:	85 c0                	test   %eax,%eax
 41e:	7f dc                	jg     3fc <memmove+0x14>
  return vdst;
 420:	8b 45 08             	mov    0x8(%ebp),%eax
}
 423:	c9                   	leave  
 424:	c3                   	ret    

00000425 <fork>:
  name: \
    movl $SYS_ ## name, %eax; \
    int $T_SYSCALL; \
    ret

SYSCALL(fork)
 425:	b8 01 00 00 00       	mov    $0x1,%eax
 42a:	cd 40                	int    $0x40
 42c:	c3                   	ret    

0000042d <exit>:
SYSCALL(exit)
 42d:	b8 02 00 00 00       	mov    $0x2,%eax
 432:	cd 40                	int    $0x40
 434:	c3                   	ret    

00000435 <wait>:
SYSCALL(wait)
 435:	b8 03 00 00 00       	mov    $0x3,%eax
 43a:	cd 40                	int    $0x40
 43c:	c3                   	ret    

0000043d <pipe>:
SYSCALL(pipe)
 43d:	b8 04 00 00 00       	mov    $0x4,%eax
 442:	cd 40                	int    $0x40
 444:	c3                   	ret    

00000445 <read>:
SYSCALL(read)
 445:	b8 05 00 00 00       	mov    $0x5,%eax
 44a:	cd 40                	int    $0x40
 44c:	c3                   	ret    

0000044d <write>:
SYSCALL(write)
 44d:	b8 10 00 00 00       	mov    $0x10,%eax
 452:	cd 40                	int    $0x40
 454:	c3                   	ret    

00000455 <close>:
SYSCALL(close)
 455:	b8 15 00 00 00       	mov    $0x15,%eax
 45a:	cd 40                	int    $0x40
 45c:	c3                   	ret    

0000045d <kill>:
SYSCALL(kill)
 45d:	b8 06 00 00 00       	mov    $0x6,%eax
 462:	cd 40                	int    $0x40
 464:	c3                   	ret    

00000465 <exec>:
SYSCALL(exec)
 465:	b8 07 00 00 00       	mov    $0x7,%eax
 46a:	cd 40                	int    $0x40
 46c:	c3                   	ret    

0000046d <open>:
SYSCALL(open)
 46d:	b8 0f 00 00 00       	mov    $0xf,%eax
 472:	cd 40                	int    $0x40
 474:	c3                   	ret    

00000475 <mknod>:
SYSCALL(mknod)
 475:	b8 11 00 00 00       	mov    $0x11,%eax
 47a:	cd 40                	int    $0x40
 47c:	c3                   	ret    

0000047d <unlink>:
SYSCALL(unlink)
 47d:	b8 12 00 00 00       	mov    $0x12,%eax
 482:	cd 40                	int    $0x40
 484:	c3                   	ret    

00000485 <fstat>:
SYSCALL(fstat)
 485:	b8 08 00 00 00       	mov    $0x8,%eax
 48a:	cd 40                	int    $0x40
 48c:	c3                   	ret    

0000048d <link>:
SYSCALL(link)
 48d:	b8 13 00 00 00       	mov    $0x13,%eax
 492:	cd 40                	int    $0x40
 494:	c3                   	ret    

00000495 <mkdir>:
SYSCALL(mkdir)
 495:	b8 14 00 00 00       	mov    $0x14,%eax
 49a:	cd 40                	int    $0x40
 49c:	c3                   	ret    

0000049d <chdir>:
SYSCALL(chdir)
 49d:	b8 09 00 00 00       	mov    $0x9,%eax
 4a2:	cd 40                	int    $0x40
 4a4:	c3                   	ret    

000004a5 <dup>:
SYSCALL(dup)
 4a5:	b8 0a 00 00 00       	mov    $0xa,%eax
 4aa:	cd 40                	int    $0x40
 4ac:	c3                   	ret    

000004ad <getpid>:
SYSCALL(getpid)
 4ad:	b8 0b 00 00 00       	mov    $0xb,%eax
 4b2:	cd 40                	int    $0x40
 4b4:	c3                   	ret    

000004b5 <sbrk>:
SYSCALL(sbrk)
 4b5:	b8 0c 00 00 00       	mov    $0xc,%eax
 4ba:	cd 40                	int    $0x40
 4bc:	c3                   	ret    

000004bd <sleep>:
SYSCALL(sleep)
 4bd:	b8 0d 00 00 00       	mov    $0xd,%eax
 4c2:	cd 40                	int    $0x40
 4c4:	c3                   	ret    

000004c5 <uptime>:
SYSCALL(uptime)
 4c5:	b8 0e 00 00 00       	mov    $0xe,%eax
 4ca:	cd 40                	int    $0x40
 4cc:	c3                   	ret    

000004cd <wait2>:
SYSCALL(wait2)
 4cd:	b8 16 00 00 00       	mov    $0x16,%eax
 4d2:	cd 40                	int    $0x40
 4d4:	c3                   	ret    

000004d5 <putc>:
#include "stat.h"
#include "user.h"

static void
putc(int fd, char c)
{
 4d5:	55                   	push   %ebp
 4d6:	89 e5                	mov    %esp,%ebp
 4d8:	83 ec 18             	sub    $0x18,%esp
 4db:	8b 45 0c             	mov    0xc(%ebp),%eax
 4de:	88 45 f4             	mov    %al,-0xc(%ebp)
  write(fd, &c, 1);
 4e1:	83 ec 04             	sub    $0x4,%esp
 4e4:	6a 01                	push   $0x1
 4e6:	8d 45 f4             	lea    -0xc(%ebp),%eax
 4e9:	50                   	push   %eax
 4ea:	ff 75 08             	push   0x8(%ebp)
 4ed:	e8 5b ff ff ff       	call   44d <write>
 4f2:	83 c4 10             	add    $0x10,%esp
}
 4f5:	90                   	nop
 4f6:	c9                   	leave  
 4f7:	c3                   	ret    

000004f8 <printint>:

static void
printint(int fd, int xx, int base, int sgn)
{
 4f8:	55                   	push   %ebp
 4f9:	89 e5                	mov    %esp,%ebp
 4fb:	83 ec 28             	sub    $0x28,%esp
  static char digits[] = "0123456789ABCDEF";
  char buf[16];
  int i, neg;
  uint x;

  neg = 0;
 4fe:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
  if(sgn && xx < 0){
 505:	83 7d 14 00          	cmpl   $0x0,0x14(%ebp)
 509:	74 17                	je     522 <printint+0x2a>
 50b:	83 7d 0c 00          	cmpl   $0x0,0xc(%ebp)
 50f:	79 11                	jns    522 <printint+0x2a>
    neg = 1;
 511:	c7 45 f0 01 00 00 00 	movl   $0x1,-0x10(%ebp)
    x = -xx;
 518:	8b 45 0c             	mov    0xc(%ebp),%eax
 51b:	f7 d8                	neg    %eax
 51d:	89 45 ec             	mov    %eax,-0x14(%ebp)
 520:	eb 06                	jmp    528 <printint+0x30>
  } else {
    x = xx;
 522:	8b 45 0c             	mov    0xc(%ebp),%eax
 525:	89 45 ec             	mov    %eax,-0x14(%ebp)
  }

  i = 0;
 528:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%ebp)
  do{
    buf[i++] = digits[x % base];
 52f:	8b 4d 10             	mov    0x10(%ebp),%ecx
 532:	8b 45 ec             	mov    -0x14(%ebp),%eax
 535:	ba 00 00 00 00       	mov    $0x0,%edx
 53a:	f7 f1                	div    %ecx
 53c:	89 d1                	mov    %edx,%ecx
 53e:	8b 45 f4             	mov    -0xc(%ebp),%eax
 541:	8d 50 01             	lea    0x1(%eax),%edx
 544:	89 55 f4             	mov    %edx,-0xc(%ebp)
 547:	0f b6 91 ec 0c 00 00 	movzbl 0xcec(%ecx),%edx
 54e:	88 54 05 dc          	mov    %dl,-0x24(%ebp,%eax,1)
  }while((x /= base) != 0);
 552:	8b 4d 10             	mov    0x10(%ebp),%ecx
 555:	8b 45 ec             	mov    -0x14(%ebp),%eax
 558:	ba 00 00 00 00       	mov    $0x0,%edx
 55d:	f7 f1                	div    %ecx
 55f:	89 45 ec             	mov    %eax,-0x14(%ebp)
 562:	83 7d ec 00          	cmpl   $0x0,-0x14(%ebp)
 566:	75 c7                	jne    52f <printint+0x37>
  if(neg)
 568:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 56c:	74 2d                	je     59b <printint+0xa3>
    buf[i++] = '-';
 56e:	8b 45 f4             	mov    -0xc(%ebp),%eax
 571:	8d 50 01             	lea    0x1(%eax),%edx
 574:	89 55 f4             	mov    %edx,-0xc(%ebp)
 577:	c6 44 05 dc 2d       	movb   $0x2d,-0x24(%ebp,%eax,1)

  while(--i >= 0)
 57c:	eb 1d                	jmp    59b <printint+0xa3>
    putc(fd, buf[i]);
 57e:	8d 55 dc             	lea    -0x24(%ebp),%edx
 581:	8b 45 f4             	mov    -0xc(%ebp),%eax
 584:	01 d0                	add    %edx,%eax
 586:	0f b6 00             	movzbl (%eax),%eax
 589:	0f be c0             	movsbl %al,%eax
 58c:	83 ec 08             	sub    $0x8,%esp
 58f:	50                   	push   %eax
 590:	ff 75 08             	push   0x8(%ebp)
 593:	e8 3d ff ff ff       	call   4d5 <putc>
 598:	83 c4 10             	add    $0x10,%esp
  while(--i >= 0)
 59b:	83 6d f4 01          	subl   $0x1,-0xc(%ebp)
 59f:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 5a3:	79 d9                	jns    57e <printint+0x86>
}
 5a5:	90                   	nop
 5a6:	90                   	nop
 5a7:	c9                   	leave  
 5a8:	c3                   	ret    

000005a9 <printf>:

// Print to the given fd. Only understands %d, %x, %p, %s.
void
printf(int fd, const char *fmt, ...)
{
 5a9:	55                   	push   %ebp
 5aa:	89 e5                	mov    %esp,%ebp
 5ac:	83 ec 28             	sub    $0x28,%esp
  char *s;
  int c, i, state;
  uint *ap;

  state = 0;
 5af:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
  ap = (uint*)(void*)&fmt + 1;
 5b6:	8d 45 0c             	lea    0xc(%ebp),%eax
 5b9:	83 c0 04             	add    $0x4,%eax
 5bc:	89 45 e8             	mov    %eax,-0x18(%ebp)
  for(i = 0; fmt[i]; i++){
 5bf:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%ebp)
 5c6:	e9 59 01 00 00       	jmp    724 <printf+0x17b>
    c = fmt[i] & 0xff;
 5cb:	8b 55 0c             	mov    0xc(%ebp),%edx
 5ce:	8b 45 f0             	mov    -0x10(%ebp),%eax
 5d1:	01 d0                	add    %edx,%eax
 5d3:	0f b6 00             	movzbl (%eax),%eax
 5d6:	0f be c0             	movsbl %al,%eax
 5d9:	25 ff 00 00 00       	and    $0xff,%eax
 5de:	89 45 e4             	mov    %eax,-0x1c(%ebp)
    if(state == 0){
 5e1:	83 7d ec 00          	cmpl   $0x0,-0x14(%ebp)
 5e5:	75 2c                	jne    613 <printf+0x6a>
      if(c == '%'){
 5e7:	83 7d e4 25          	cmpl   $0x25,-0x1c(%ebp)
 5eb:	75 0c                	jne    5f9 <printf+0x50>
        state = '%';
 5ed:	c7 45 ec 25 00 00 00 	movl   $0x25,-0x14(%ebp)
 5f4:	e9 27 01 00 00       	jmp    720 <printf+0x177>
      } else {
        putc(fd, c);
 5f9:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 5fc:	0f be c0             	movsbl %al,%eax
 5ff:	83 ec 08             	sub    $0x8,%esp
 602:	50                   	push   %eax
 603:	ff 75 08             	push   0x8(%ebp)
 606:	e8 ca fe ff ff       	call   4d5 <putc>
 60b:	83 c4 10             	add    $0x10,%esp
 60e:	e9 0d 01 00 00       	jmp    720 <printf+0x177>
      }
    } else if(state == '%'){
 613:	83 7d ec 25          	cmpl   $0x25,-0x14(%ebp)
 617:	0f 85 03 01 00 00    	jne    720 <printf+0x177>
      if(c == 'd'){
 61d:	83 7d e4 64          	cmpl   $0x64,-0x1c(%ebp)
 621:	75 1e                	jne    641 <printf+0x98>
        printint(fd, *ap, 10, 1);
 623:	8b 45 e8             	mov    -0x18(%ebp),%eax
 626:	8b 00                	mov    (%eax),%eax
 628:	6a 01                	push   $0x1
 62a:	6a 0a                	push   $0xa
 62c:	50                   	push   %eax
 62d:	ff 75 08             	push   0x8(%ebp)
 630:	e8 c3 fe ff ff       	call   4f8 <printint>
 635:	83 c4 10             	add    $0x10,%esp
        ap++;
 638:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 63c:	e9 d8 00 00 00       	jmp    719 <printf+0x170>
      } else if(c == 'x' || c == 'p'){
 641:	83 7d e4 78          	cmpl   $0x78,-0x1c(%ebp)
 645:	74 06                	je     64d <printf+0xa4>
 647:	83 7d e4 70          	cmpl   $0x70,-0x1c(%ebp)
 64b:	75 1e                	jne    66b <printf+0xc2>
        printint(fd, *ap, 16, 0);
 64d:	8b 45 e8             	mov    -0x18(%ebp),%eax
 650:	8b 00                	mov    (%eax),%eax
 652:	6a 00                	push   $0x0
 654:	6a 10                	push   $0x10
 656:	50                   	push   %eax
 657:	ff 75 08             	push   0x8(%ebp)
 65a:	e8 99 fe ff ff       	call   4f8 <printint>
 65f:	83 c4 10             	add    $0x10,%esp
        ap++;
 662:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 666:	e9 ae 00 00 00       	jmp    719 <printf+0x170>
      } else if(c == 's'){
 66b:	83 7d e4 73          	cmpl   $0x73,-0x1c(%ebp)
 66f:	75 43                	jne    6b4 <printf+0x10b>
        s = (char*)*ap;
 671:	8b 45 e8             	mov    -0x18(%ebp),%eax
 674:	8b 00                	mov    (%eax),%eax
 676:	89 45 f4             	mov    %eax,-0xc(%ebp)
        ap++;
 679:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
        if(s == 0)
 67d:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 681:	75 25                	jne    6a8 <printf+0xff>
          s = "(null)";
 683:	c7 45 f4 a0 0a 00 00 	movl   $0xaa0,-0xc(%ebp)
        while(*s != 0){
 68a:	eb 1c                	jmp    6a8 <printf+0xff>
          putc(fd, *s);
 68c:	8b 45 f4             	mov    -0xc(%ebp),%eax
 68f:	0f b6 00             	movzbl (%eax),%eax
 692:	0f be c0             	movsbl %al,%eax
 695:	83 ec 08             	sub    $0x8,%esp
 698:	50                   	push   %eax
 699:	ff 75 08             	push   0x8(%ebp)
 69c:	e8 34 fe ff ff       	call   4d5 <putc>
 6a1:	83 c4 10             	add    $0x10,%esp
          s++;
 6a4:	83 45 f4 01          	addl   $0x1,-0xc(%ebp)
        while(*s != 0){
 6a8:	8b 45 f4             	mov    -0xc(%ebp),%eax
 6ab:	0f b6 00             	movzbl (%eax),%eax
 6ae:	84 c0                	test   %al,%al
 6b0:	75 da                	jne    68c <printf+0xe3>
 6b2:	eb 65                	jmp    719 <printf+0x170>
        }
      } else if(c == 'c'){
 6b4:	83 7d e4 63          	cmpl   $0x63,-0x1c(%ebp)
 6b8:	75 1d                	jne    6d7 <printf+0x12e>
        putc(fd, *ap);
 6ba:	8b 45 e8             	mov    -0x18(%ebp),%eax
 6bd:	8b 00                	mov    (%eax),%eax
 6bf:	0f be c0             	movsbl %al,%eax
 6c2:	83 ec 08             	sub    $0x8,%esp
 6c5:	50                   	push   %eax
 6c6:	ff 75 08             	push   0x8(%ebp)
 6c9:	e8 07 fe ff ff       	call   4d5 <putc>
 6ce:	83 c4 10             	add    $0x10,%esp
        ap++;
 6d1:	83 45 e8 04          	addl   $0x4,-0x18(%ebp)
 6d5:	eb 42                	jmp    719 <printf+0x170>
      } else if(c == '%'){
 6d7:	83 7d e4 25          	cmpl   $0x25,-0x1c(%ebp)
 6db:	75 17                	jne    6f4 <printf+0x14b>
        putc(fd, c);
 6dd:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 6e0:	0f be c0             	movsbl %al,%eax
 6e3:	83 ec 08             	sub    $0x8,%esp
 6e6:	50                   	push   %eax
 6e7:	ff 75 08             	push   0x8(%ebp)
 6ea:	e8 e6 fd ff ff       	call   4d5 <putc>
 6ef:	83 c4 10             	add    $0x10,%esp
 6f2:	eb 25                	jmp    719 <printf+0x170>
      } else {
        // Unknown % sequence.  Print it to draw attention.
        putc(fd, '%');
 6f4:	83 ec 08             	sub    $0x8,%esp
 6f7:	6a 25                	push   $0x25
 6f9:	ff 75 08             	push   0x8(%ebp)
 6fc:	e8 d4 fd ff ff       	call   4d5 <putc>
 701:	83 c4 10             	add    $0x10,%esp
        putc(fd, c);
 704:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 707:	0f be c0             	movsbl %al,%eax
 70a:	83 ec 08             	sub    $0x8,%esp
 70d:	50                   	push   %eax
 70e:	ff 75 08             	push   0x8(%ebp)
 711:	e8 bf fd ff ff       	call   4d5 <putc>
 716:	83 c4 10             	add    $0x10,%esp
      }
      state = 0;
 719:	c7 45 ec 00 00 00 00 	movl   $0x0,-0x14(%ebp)
  for(i = 0; fmt[i]; i++){
 720:	83 45 f0 01          	addl   $0x1,-0x10(%ebp)
 724:	8b 55 0c             	mov    0xc(%ebp),%edx
 727:	8b 45 f0             	mov    -0x10(%ebp),%eax
 72a:	01 d0                	add    %edx,%eax
 72c:	0f b6 00             	movzbl (%eax),%eax
 72f:	84 c0                	test   %al,%al
 731:	0f 85 94 fe ff ff    	jne    5cb <printf+0x22>
    }
  }
}
 737:	90                   	nop
 738:	90                   	nop
 739:	c9                   	leave  
 73a:	c3                   	ret    

0000073b <free>:
static Header base;
static Header *freep;

void
free(void *ap)
{
 73b:	55                   	push   %ebp
 73c:	89 e5                	mov    %esp,%ebp
 73e:	83 ec 10             	sub    $0x10,%esp
  Header *bp, *p;

  bp = (Header*)ap - 1;
 741:	8b 45 08             	mov    0x8(%ebp),%eax
 744:	83 e8 08             	sub    $0x8,%eax
 747:	89 45 f8             	mov    %eax,-0x8(%ebp)
  for(p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
 74a:	a1 08 0d 00 00       	mov    0xd08,%eax
 74f:	89 45 fc             	mov    %eax,-0x4(%ebp)
 752:	eb 24                	jmp    778 <free+0x3d>
    if(p >= p->s.ptr && (bp > p || bp < p->s.ptr))
 754:	8b 45 fc             	mov    -0x4(%ebp),%eax
 757:	8b 00                	mov    (%eax),%eax
 759:	39 45 fc             	cmp    %eax,-0x4(%ebp)
 75c:	72 12                	jb     770 <free+0x35>
 75e:	8b 45 f8             	mov    -0x8(%ebp),%eax
 761:	3b 45 fc             	cmp    -0x4(%ebp),%eax
 764:	77 24                	ja     78a <free+0x4f>
 766:	8b 45 fc             	mov    -0x4(%ebp),%eax
 769:	8b 00                	mov    (%eax),%eax
 76b:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 76e:	72 1a                	jb     78a <free+0x4f>
  for(p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
 770:	8b 45 fc             	mov    -0x4(%ebp),%eax
 773:	8b 00                	mov    (%eax),%eax
 775:	89 45 fc             	mov    %eax,-0x4(%ebp)
 778:	8b 45 f8             	mov    -0x8(%ebp),%eax
 77b:	3b 45 fc             	cmp    -0x4(%ebp),%eax
 77e:	76 d4                	jbe    754 <free+0x19>
 780:	8b 45 fc             	mov    -0x4(%ebp),%eax
 783:	8b 00                	mov    (%eax),%eax
 785:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 788:	73 ca                	jae    754 <free+0x19>
      break;
  if(bp + bp->s.size == p->s.ptr){
 78a:	8b 45 f8             	mov    -0x8(%ebp),%eax
 78d:	8b 40 04             	mov    0x4(%eax),%eax
 790:	8d 14 c5 00 00 00 00 	lea    0x0(,%eax,8),%edx
 797:	8b 45 f8             	mov    -0x8(%ebp),%eax
 79a:	01 c2                	add    %eax,%edx
 79c:	8b 45 fc             	mov    -0x4(%ebp),%eax
 79f:	8b 00                	mov    (%eax),%eax
 7a1:	39 c2                	cmp    %eax,%edx
 7a3:	75 24                	jne    7c9 <free+0x8e>
    bp->s.size += p->s.ptr->s.size;
 7a5:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7a8:	8b 50 04             	mov    0x4(%eax),%edx
 7ab:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7ae:	8b 00                	mov    (%eax),%eax
 7b0:	8b 40 04             	mov    0x4(%eax),%eax
 7b3:	01 c2                	add    %eax,%edx
 7b5:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7b8:	89 50 04             	mov    %edx,0x4(%eax)
    bp->s.ptr = p->s.ptr->s.ptr;
 7bb:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7be:	8b 00                	mov    (%eax),%eax
 7c0:	8b 10                	mov    (%eax),%edx
 7c2:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7c5:	89 10                	mov    %edx,(%eax)
 7c7:	eb 0a                	jmp    7d3 <free+0x98>
  } else
    bp->s.ptr = p->s.ptr;
 7c9:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7cc:	8b 10                	mov    (%eax),%edx
 7ce:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7d1:	89 10                	mov    %edx,(%eax)
  if(p + p->s.size == bp){
 7d3:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7d6:	8b 40 04             	mov    0x4(%eax),%eax
 7d9:	8d 14 c5 00 00 00 00 	lea    0x0(,%eax,8),%edx
 7e0:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7e3:	01 d0                	add    %edx,%eax
 7e5:	39 45 f8             	cmp    %eax,-0x8(%ebp)
 7e8:	75 20                	jne    80a <free+0xcf>
    p->s.size += bp->s.size;
 7ea:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7ed:	8b 50 04             	mov    0x4(%eax),%edx
 7f0:	8b 45 f8             	mov    -0x8(%ebp),%eax
 7f3:	8b 40 04             	mov    0x4(%eax),%eax
 7f6:	01 c2                	add    %eax,%edx
 7f8:	8b 45 fc             	mov    -0x4(%ebp),%eax
 7fb:	89 50 04             	mov    %edx,0x4(%eax)
    p->s.ptr = bp->s.ptr;
 7fe:	8b 45 f8             	mov    -0x8(%ebp),%eax
 801:	8b 10                	mov    (%eax),%edx
 803:	8b 45 fc             	mov    -0x4(%ebp),%eax
 806:	89 10                	mov    %edx,(%eax)
 808:	eb 08                	jmp    812 <free+0xd7>
  } else
    p->s.ptr = bp;
 80a:	8b 45 fc             	mov    -0x4(%ebp),%eax
 80d:	8b 55 f8             	mov    -0x8(%ebp),%edx
 810:	89 10                	mov    %edx,(%eax)
  freep = p;
 812:	8b 45 fc             	mov    -0x4(%ebp),%eax
 815:	a3 08 0d 00 00       	mov    %eax,0xd08
}
 81a:	90                   	nop
 81b:	c9                   	leave  
 81c:	c3                   	ret    

0000081d <morecore>:

static Header*
morecore(uint nu)
{
 81d:	55                   	push   %ebp
 81e:	89 e5                	mov    %esp,%ebp
 820:	83 ec 18             	sub    $0x18,%esp
  char *p;
  Header *hp;

  if(nu < 4096)
 823:	81 7d 08 ff 0f 00 00 	cmpl   $0xfff,0x8(%ebp)
 82a:	77 07                	ja     833 <morecore+0x16>
    nu = 4096;
 82c:	c7 45 08 00 10 00 00 	movl   $0x1000,0x8(%ebp)
  p = sbrk(nu * sizeof(Header));
 833:	8b 45 08             	mov    0x8(%ebp),%eax
 836:	c1 e0 03             	shl    $0x3,%eax
 839:	83 ec 0c             	sub    $0xc,%esp
 83c:	50                   	push   %eax
 83d:	e8 73 fc ff ff       	call   4b5 <sbrk>
 842:	83 c4 10             	add    $0x10,%esp
 845:	89 45 f4             	mov    %eax,-0xc(%ebp)
  if(p == (char*)-1)
 848:	83 7d f4 ff          	cmpl   $0xffffffff,-0xc(%ebp)
 84c:	75 07                	jne    855 <morecore+0x38>
    return 0;
 84e:	b8 00 00 00 00       	mov    $0x0,%eax
 853:	eb 26                	jmp    87b <morecore+0x5e>
  hp = (Header*)p;
 855:	8b 45 f4             	mov    -0xc(%ebp),%eax
 858:	89 45 f0             	mov    %eax,-0x10(%ebp)
  hp->s.size = nu;
 85b:	8b 45 f0             	mov    -0x10(%ebp),%eax
 85e:	8b 55 08             	mov    0x8(%ebp),%edx
 861:	89 50 04             	mov    %edx,0x4(%eax)
  free((void*)(hp + 1));
 864:	8b 45 f0             	mov    -0x10(%ebp),%eax
 867:	83 c0 08             	add    $0x8,%eax
 86a:	83 ec 0c             	sub    $0xc,%esp
 86d:	50                   	push   %eax
 86e:	e8 c8 fe ff ff       	call   73b <free>
 873:	83 c4 10             	add    $0x10,%esp
  return freep;
 876:	a1 08 0d 00 00       	mov    0xd08,%eax
}
 87b:	c9                   	leave  
 87c:	c3                   	ret    

0000087d <malloc>:

void*
malloc(uint nbytes)
{
 87d:	55                   	push   %ebp
 87e:	89 e5                	mov    %esp,%ebp
 880:	83 ec 18             	sub    $0x18,%esp
  Header *p, *prevp;
  uint nunits;

  nunits = (nbytes + sizeof(Header) - 1)/sizeof(Header) + 1;
 883:	8b 45 08             	mov    0x8(%ebp),%eax
 886:	83 c0 07             	add    $0x7,%eax
 889:	c1 e8 03             	shr    $0x3,%eax
 88c:	83 c0 01             	add    $0x1,%eax
 88f:	89 45 ec             	mov    %eax,-0x14(%ebp)
  if((prevp = freep) == 0){
 892:	a1 08 0d 00 00       	mov    0xd08,%eax
 897:	89 45 f0             	mov    %eax,-0x10(%ebp)
 89a:	83 7d f0 00          	cmpl   $0x0,-0x10(%ebp)
 89e:	75 23                	jne    8c3 <malloc+0x46>
    base.s.ptr = freep = prevp = &base;
 8a0:	c7 45 f0 00 0d 00 00 	movl   $0xd00,-0x10(%ebp)
 8a7:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8aa:	a3 08 0d 00 00       	mov    %eax,0xd08
 8af:	a1 08 0d 00 00       	mov    0xd08,%eax
 8b4:	a3 00 0d 00 00       	mov    %eax,0xd00
    base.s.size = 0;
 8b9:	c7 05 04 0d 00 00 00 	movl   $0x0,0xd04
 8c0:	00 00 00 
  }
  for(p = prevp->s.ptr; ; prevp = p, p = p->s.ptr){
 8c3:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8c6:	8b 00                	mov    (%eax),%eax
 8c8:	89 45 f4             	mov    %eax,-0xc(%ebp)
    if(p->s.size >= nunits){
 8cb:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8ce:	8b 40 04             	mov    0x4(%eax),%eax
 8d1:	39 45 ec             	cmp    %eax,-0x14(%ebp)
 8d4:	77 4d                	ja     923 <malloc+0xa6>
      if(p->s.size == nunits)
 8d6:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8d9:	8b 40 04             	mov    0x4(%eax),%eax
 8dc:	39 45 ec             	cmp    %eax,-0x14(%ebp)
 8df:	75 0c                	jne    8ed <malloc+0x70>
        prevp->s.ptr = p->s.ptr;
 8e1:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8e4:	8b 10                	mov    (%eax),%edx
 8e6:	8b 45 f0             	mov    -0x10(%ebp),%eax
 8e9:	89 10                	mov    %edx,(%eax)
 8eb:	eb 26                	jmp    913 <malloc+0x96>
      else {
        p->s.size -= nunits;
 8ed:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8f0:	8b 40 04             	mov    0x4(%eax),%eax
 8f3:	2b 45 ec             	sub    -0x14(%ebp),%eax
 8f6:	89 c2                	mov    %eax,%edx
 8f8:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8fb:	89 50 04             	mov    %edx,0x4(%eax)
        p += p->s.size;
 8fe:	8b 45 f4             	mov    -0xc(%ebp),%eax
 901:	8b 40 04             	mov    0x4(%eax),%eax
 904:	c1 e0 03             	shl    $0x3,%eax
 907:	01 45 f4             	add    %eax,-0xc(%ebp)
        p->s.size = nunits;
 90a:	8b 45 f4             	mov    -0xc(%ebp),%eax
 90d:	8b 55 ec             	mov    -0x14(%ebp),%edx
 910:	89 50 04             	mov    %edx,0x4(%eax)
      }
      freep = prevp;
 913:	8b 45 f0             	mov    -0x10(%ebp),%eax
 916:	a3 08 0d 00 00       	mov    %eax,0xd08
      return (void*)(p + 1);
 91b:	8b 45 f4             	mov    -0xc(%ebp),%eax
 91e:	83 c0 08             	add    $0x8,%eax
 921:	eb 3b                	jmp    95e <malloc+0xe1>
    }
    if(p == freep)
 923:	a1 08 0d 00 00       	mov    0xd08,%eax
 928:	39 45 f4             	cmp    %eax,-0xc(%ebp)
 92b:	75 1e                	jne    94b <malloc+0xce>
      if((p = morecore(nunits)) == 0)
 92d:	83 ec 0c             	sub    $0xc,%esp
 930:	ff 75 ec             	push   -0x14(%ebp)
 933:	e8 e5 fe ff ff       	call   81d <morecore>
 938:	83 c4 10             	add    $0x10,%esp
 93b:	89 45 f4             	mov    %eax,-0xc(%ebp)
 93e:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)
 942:	75 07                	jne    94b <malloc+0xce>
        return 0;
 944:	b8 00 00 00 00       	mov    $0x0,%eax
 949:	eb 13                	jmp    95e <malloc+0xe1>
  for(p = prevp->s.ptr; ; prevp = p, p = p->s.ptr){
 94b:	8b 45 f4             	mov    -0xc(%ebp),%eax
 94e:	89 45 f0             	mov    %eax,-0x10(%ebp)
 951:	8b 45 f4             	mov    -0xc(%ebp),%eax
 954:	8b 00                	mov    (%eax),%eax
 956:	89 45 f4             	mov    %eax,-0xc(%ebp)
    if(p->s.size >= nunits){
 959:	e9 6d ff ff ff       	jmp    8cb <malloc+0x4e>
  }
}
 95e:	c9                   	leave  
 95f:	c3                   	ret    
