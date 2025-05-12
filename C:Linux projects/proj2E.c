

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


































int main(int argc, char *argv[]) {
    // check command line arguments
    if (argc < 3) {
        printf("usage: %s <input file> <word1> <word2> ...\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // open file
    FILE *f_in = fopen(argv[1], "r");
    if (f_in == NULL) {
        printf("%s is not a valid file\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    // get file size
    fseek(f_in, 0, SEEK_END);
    int buffer_size = ftell(f_in);
    fseek(f_in, 0, SEEK_SET);

    // allocate memory for buffer
    char *buffer = malloc(buffer_size);
   

    // read file into buffer
    fread(buffer, sizeof(char), buffer_size, f_in);

    int *counter = malloc(argc - 2);
    for (int g = 0; g < argc - 2; g++){
        counter[g] = 0;
    }

// seperate words
    for (int i = 0; i < buffer_size; i++) {
        if (buffer[i] == ',') {
            buffer[i] = '\0';
        }
        if (buffer[i] == ' ') {
            buffer[i] = '\0';
        }
        if (buffer[i] == '.') {
            buffer[i] = '\0';
        }
        if (buffer[i] == '\n') {
            buffer[i] = '\0';
        }
        if (buffer[i] == EOF) {
            buffer[i] = '\0';
        }
    }
    
    for (int j = 0; j < buffer_size; j++){
        for (int k = 0; k < argc - 2; k++){
            int length = strlen(argv[k+2]);
            if (strncmp(buffer+j, argv[k+2], length) == 0){
            }
                if (*(buffer+j-1) == '\0' && *(buffer+j+length) == '\0'){
                    counter[k]++;
        }
    }
    }
    // close file
    fclose(f_in);

    // count occurrences of each word
    for (int i = 2; i < argc; i++) {

        printf("The word \"%s\" occurs %d times.\n", argv, counter[i]);
    }
    fclose(f_in);
    free(buffer);
    free(counter);

    return 0;
}