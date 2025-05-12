#include <stdio.h>
#include <stdlib.h> // Add this line to include the necessary header file for fopen and fclose functions

int main(int argc, char* argv[]){
    // write a mtrix to a file
    // read back that data
    int* matrix = (int*)malloc(10 * sizeof(int));


    for(int i = 0; i < 10; i++){
        matrix[i] = i;

    }
    for (int i = 0; i < 10; i++){
        printf("%d", matrix[i]);
    }
    printf("\n");

    char * filename = "matrix_file";
    FILE* file_pointer = fopen(filename, "w");

    //method 1
    for (int i = 0; i < 10; i++){
        if(fwrite(&matrix[i], sizeof(int), 1, file_pointer) != 1){ //using the address of the matrix bc our strings are pointers
            printf("error");
        }
    }   
    fwrite(matrix, sizeof(int), 10, file_pointer);
    
    fclose(file_pointer);
    
    file_pointer = fopen(filename, "r");
    
    int* buffer[10];
    
    fread(buffer, sizeof(int), 10, file_pointer);
    printf("found in file: ");
    for (int i = 0; i < 10; i++){
        printf("%d", buffer[i]);
    }
}