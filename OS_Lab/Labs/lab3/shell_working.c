#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

#define MAX_INPUT_SIZE 1024
#define MAX_TOKEN_SIZE 64
#define MAX_NUM_TOKENS 64

// TODO: YOUR CODE HERE
// INITIALIZE DATA STRUCTURE TO STORE PIDS OF PROCESSES TO KILL LATER

/* Splits the string by space and returns the array of tokens
*
*/
char **tokenize(char *line) {

    // tokenizer variables
	char **tokens = (char **)malloc(MAX_NUM_TOKENS * sizeof(char *));
	char *token = (char *)malloc(MAX_TOKEN_SIZE * sizeof(char));
	int i, tokenIndex = 0, tokenNo = 0;

    // loop on length of line
	for(i=0; i < strlen(line); i++){

		char readChar = line[i];

        // tokenize on any kind of space
		if (readChar == ' ' || readChar == '\n' || readChar == '\t'){
			token[tokenIndex] = '\0';
			if (tokenIndex != 0) {
				tokens[tokenNo] = (char*)malloc(MAX_TOKEN_SIZE*sizeof(char));
				strcpy(tokens[tokenNo++], token);
				tokenIndex = 0; 
			}
		}
		else {
			token[tokenIndex++] = readChar;
		}
	}
	
	free(token);
	tokens[tokenNo] = NULL ;
	return tokens;
}

// TODO
// MAKE FUNCTIONS AS REQUIRED TO AVOID REPETITIVE WORK

int main(int argc, char* argv[]) {

	char  line[MAX_INPUT_SIZE];            
	char  **tokens;           
	
	// TODO: YOUR CODE HERE
	// INITIALIZE GLOBAL DATA STRUCTURE OF PIDS TO SOME DEFAULT VALUE  
	// INITIALIZE OTHER VARIABLES AS NEEDED

	while(1) {	

		/* BEGIN: TAKING INPUT */
		bzero(line, sizeof(line));
		printf("$ ");
		scanf("%[^\n]", line);
		getchar();
		/* END: TAKING INPUT */

		line[strlen(line)] = '\n'; //terminate with new line
		tokens = tokenize(line);
		int an=0;
		int sz=0;
        char* dir="cd";
		char* hh="&&";
		for(int i=0;tokens[i]!=NULL;i++){
			// printf("%d\n",i);
			// printf("%s\n",tokens[i]);
			if(!(strcmp(tokens[i],hh))){
				an=i;
				
			}
			sz++;
		}
		sz--;
		int x=fork();
		if(x==0){
			if(an==0){
			execvp(tokens[an],&tokens[an]);
			exit(0);
			}else{
				int x2=fork();
				// printf("%d\n",x2);
				if(x2==0){
				char* arr[an+1];
				for(int i=0;i<an;i++){
					arr[i]=tokens[i];
					// printf("i-%d  str-%s",i,arr[i]);
				}
				arr[an]=NULL;
                if(strcmp(arr[0],dir)){
				execvp(arr[0],arr);}
				exit(0);
				
				}else{
				wait(NULL);
                if(strcmp(tokens[an+1],dir)){
				execvp(tokens[an+1],&tokens[an+1]);}
				exit(0);
				
				}
			}
		}else{
			wait(NULL);
            if(!strcmp(tokens[0],dir)  ){
                tokens[an]=NULL;
                chdir(tokens[1]);

            }
            if(!strcmp(tokens[an+1],dir)){
                chdir(tokens[an+2]);
            }
			
		}
		
		// You can maintain boolean variables to check which type of command is given by user and then
        // conditionally execute depending on them


        // TODO: YOUR CODE HERE
        //
        // TODO: YOUR CODE HERE
    
        // freeing the memory
		for(int i=0;tokens[i]!=NULL;i++){
			free(tokens[i]);
		}

		free(tokens);

	}
	return 0;
}














// #include <unistd.h>
// #include <stdio.h>

// // Main Method
// int main() {

// // changing the current
// // working directory(cwd)
// // to /usr
// if (chdir("/usr") != 0)
// 	perror("chdir() to /usr failed");

// // changing the cwd to /tmp
// if (chdir("/tmp") != 0)
// 	perror("chdir() to /temp failed");

// // there is no /error
// // directory in my pc
// if (chdir("/error") != 0)

// 	// so chdir will return -1
// 	perror("chdir() to /error failed");

// return 0;
// }


// #include <unistd.h>
// #include <stdio.h>

// // Main Method
// int main() {

// // changing the current
// // working directory(cwd)
// // to /usr
// if (chdir("/usr") != 0)
// 	perror("chdir() to /usr failed");

// // changing the cwd to /tmp
// if (chdir("/tmp") != 0)
// 	perror("chdir() to /temp failed");

// // there is no /error
// // directory in my pc
// if (chdir("/error") != 0)

// 	// so chdir will return -1
// 	perror("chdir() to /error failed");

// return 0;
// }


