#ifndef PROJ3A_QUEUE_H
#define PROJ3A_QUEUE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 8
#define MAX_STRING_LENGTH 256

//define queue structure
typedef struct{
char** array; //pointer to a pointer to a char
int front;
int rear; 
int capacity; // 8
int size;
} Queue;

void initialize(Queue* q);
void cleanup(Queue* q);
int isFull(Queue* q);
int isEmpty(Queue* q);
void resize(Queue* q);
void enqueue(Queue* q, const char* value);
char* dequeue(Queue* q);
void printQueue(Queue* q);

#endif