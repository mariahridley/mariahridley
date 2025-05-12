#include <stdio.h>
#include <stdlib.h> // Add this line to include the necessary header file for fopen and fclose functions

//write to a file from the user and read the contents of file
int main(int argc, char *argv[])
{
    if (argc != 2){
        return 1;
        
    }
    printf("file name is %s \n", argv[1]);

    char* filename = argv[1];
    
    char* mode = "w";
    
    FILE* file_pointer = fopen(filename, mode);
    
    char* hello_world = "Hello World\0";
    
    fwrite (hello_world, sizeof(char), 13, file_pointer);
    
    fclose(file_pointer);

    mode = "r";

    file_pointer = fopen(filename, mode);

    char buffer[13];

    fread(buffer, sizeof(char), 13, file_pointer);

    printf("%s \n", buffer);

    char buffer2[7];

    fseek(file_pointer, 0, 0);

    fread(buffer2, sizeof(char), 6, file_pointer);

    fclose(file_pointer);

    //insert code here

    return 0;
}

// fwrite took a pointer to where the file holds a character and we specified the amount of dtaa it'll hold
// fread stores the information in the buffer
// buffer is a pointer to the file and it reads the first 6 characters of the file