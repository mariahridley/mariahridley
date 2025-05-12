#include "proj3A_queue.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void initialize(Queue* q){
    q->array = (char**)malloc(INITIAL_CAPACITY * sizeof(char*)); //allocate memory
    q->front = 0; //front
    q->rear = 0; //rear
    q->capacity = INITIAL_CAPACITY; //capacity
    q->size = 0; //size
}

void cleanup(Queue* q){
    for (int i = 0; i < q->size; i++){ //for loop

        free(q->array[i]); //free memory
    }
    free(q->array); 
    q->array = NULL; 
    q->front = 0;
    q->rear = 0;
    q->capacity = 0;
    q->size = 0;
}

int isFull(Queue* q){
    return q->size == q->capacity;
}

int isEmpty(Queue* q){
    return q->size == 0;
}



void resize(Queue* q){
    int newCapacity = q->capacity * 2; //double capacity
    char** newArray = (char**)malloc(newCapacity * sizeof(char*)); //reallocate memory

    for (int i = 0; i < q->size; i++){ 
        int index = (q->front + i) % q->capacity;
        newArray[i] = q->array[index]; //copy array
}
    free(q->array); //free old memory
    q->array = newArray; //reassign
    q->front = 0; 
    q->rear = q->size; 
    q->capacity = newCapacity; 
    printf("Resizing queue to %d\n", newCapacity);
}



void enqueue(Queue* q, const char* value){
    if (isFull(q)){ //if full
        resize(q); 
    }
    q->array[q->rear] = (char*)malloc(MAX_STRING_LENGTH * sizeof(char)); //allocate memory
    strncpy(q->array[q->rear], value, MAX_STRING_LENGTH - 1); //copy value
    q->rear = (q->rear + 1) % q->capacity; //rear
    q->size++; //size
}




char* dequeue(Queue* q){
    if (isEmpty(q)){ //if empty
        return NULL;
    }
    char* dequeued = q->array[q->front]; //dequeue
    q->front = (q->front + 1) % q->capacity; //front
    q->size--; //size
    return dequeued; //return
}








void printQueue(Queue* q){
    
    printf("Capacity = %d, used: %d\n", q->capacity, q->size); //print
}