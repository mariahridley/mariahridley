#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "proj3A_queue.h" //include header file
#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    /* Handles command-line arguments:
- Two arguments required: an input file name and a string delimiter.
- If not provided: Please provide a file name and a delimiter.
- If the file can't be opened: Could not open file %s.

Reads the input file, tokenizes it using strtok, and interacts with the queue to:
1. First Enqueuing Pass: Add tokens to the queue and display each operation.
2. Dequeuing All Elements: Remove and display all queue entries.
3. Second Enqueuing Pass: Re-add all tokens and display operations.
4. Print Queue: Display the queue contents and its capacity and size.
5. Cleanup: Free all dynamically allocated memory.

Input file (proj3A_input.txt) contains:
vbnet
Copy code
You don't get what you wish for. You get what you work for */

if (argc < 3){ //if not provided
    printf("Please provide a file name and a delimiter.\n");
    return 1;
}

char* filename = argv[1]; //filename
char* delimiter = argv[2]; //delimiter

FILE* file = fopen(filename, "r"); //open file

if (file == NULL){ //if file can't be opened
    printf("Could not open file %s.\n", filename);
    return 1;
}
Queue q;
initialize(&q);

char buffer[BUFFER_SIZE]; //buffer
char* token; //token

printf("=> First enqueuing pass\n");
while (fgets(buffer, BUFFER_SIZE, file)){ //read file
    
    token = strtok(buffer, delimiter); //tokenize
    
    while (token != NULL){ //while token is not null
        
        printf("Enqueued (%d): %s\n", q.rear == 0 ? q.capacity - 1 : q.rear - 1, token);

        // This is a ternary operator that calculates the index of the last enqueued item.
        enqueue(&q, token); //enqueue
        token = strtok(NULL, delimiter); //tokenize
    }
}
rewind(file); 

printf("\n=> Dequeuing all elements\n");
while (!isEmpty(&q)){ //while queue is not empty
    char* dequeued = dequeue(&q); //dequeue
    printf("Dequeued (%d): %s\n", q.front == 0 ? q.capacity - 1 : q.front - 1, dequeued); //dequeue
    free(dequeued); 
}

//same as first enqueuing pas
printf("\n=> Second enqueuing pass\n");
while (fgets(buffer, BUFFER_SIZE, file)){ 
    token = strtok(buffer, delimiter); 
    while (token != NULL){ 
        printf("Enqueued (%d): %s\n", q.rear == 0 ? q.capacity - 1 : q.rear - 1, token);
        enqueue(&q, token); 
        token = strtok(NULL, delimiter); 
    }
}
printf("\n=> Printing queue\n");
printQueue(&q); //print queue

printf("\n=> Calling Queue cleanup\n");
cleanup(&q);


fclose(file);
return 0;
}

