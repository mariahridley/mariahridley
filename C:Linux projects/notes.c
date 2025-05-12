#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){

    // check command line arguments
    if (argc != 3){
        printf("usuage: %s <input file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    // define variables
    FILE *f_in; 
    int buff_size;
    char *buffer;

    f_in = fopen(argv[1], "r"); //file in read mode
    if (f_in == NULL){ //check if file exists
        printf("cannot open file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }
    fseek(f_in, 0, SEEK_END); //move to end of file
    
    buff_size = ftell(f_in); //get size of file
    
    fseek(f_in, 0, SEEK_SET); //move to start of file

    buffer = (char *)malloc(buff_size * sizeof(char)); //allocate memory for buffer
    
    fread(buffer, sizeof(char), buff_size, f_in); //read file into buffer

    

}