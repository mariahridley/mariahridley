#include <stdio.h>

int main()
{
    int A[100] = { 252, 657, 268, 402, 950, 66, 391, 285, 133, 577, 649, 166, 987,
    314, 954, 214, 920, 230, 904, 801, 40, 552, 369, 682, 202, 712, 395, 517, 755, 603,
    134, 385, 428, 941, 443, 477, 95, 647, 687, 737, 673, 19, 325, 697, 577, 181, 45,
    964, 267, 600, 858, 145, 780, 760, 949, 507, 673, 717, 446, 634, 635, 679, 466,
    474, 916, 855, 216, 899, 804, 159, 237, 625, 963, 388, 437, 682, 821, 325, 805,
    876, 968, 414, 190, 433, 902, 794, 752, 729, 77, 243, 705, 953, 765, 637, 765, 158,
    166, 599, 70, 927 };
    /* YOUR CODE GOES HERE
    * HINT: WRITE THE PRINT FUNCTION IN STEP 1 FIRST */
    int a;
    /* Step 2: SORT IT */
    for (int i = 0; i < 100 - 1; i++){
        for (int j = 0; j < 100 - i - 1; j++){
            if (A[j] > A[j+1]){
            a = A[j]; // swapping the elementsh>
            A[j] = A[j+1];
            A[j+1] = a;
            }
        }
    }

    /* Step 1: PRINT IT */
    /*The output must contain 10 rows with 10 numbers per row.
    The first column is preceded by a tab (i.e. \t) - see the correct output file.
    Each column, including the first column, must be separated using a tab (i.e., \t). The final column does not have a trailing tab.
    */

    for (int i = 0; i < 100; i++){ // Change the condition to i < 99
        if (i % 10 == 0){ //starting a new line with a tab for every 10th number
        if (i == 10){
            printf("\t");
        }else{
            printf("\n\t");
        }
        }
        if (i % 10 == 9 || i == 99) { //last element has no tab
            printf("%d", A[i]);
        }
        else{ //all other elements have a tab
            printf("%d\t", A[i]);
        }
        
    }
    printf("\n");
    return 0;
}
