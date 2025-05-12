#include <stdio.h>

int main(){
    int x = 3;
    printf("Hex: %p\n", &x);
}

/* 
gcc hexa.c -o hexa
./hex produces the hex value of the address of x?
cat hexa.c
*/

// ./filename - runs the code