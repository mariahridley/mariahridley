#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


int *AllocateArray(int N)
{
    int *A = (int *)malloc(N * sizeof(int));
    
    if(A == NULL){
        printf("no mmeory found.\n");
        exit(1);
    }
    
    for (int i = 0; i < N; i++){
        A[i] = rand() % (10 * N); //use the rand() function and a modulo operator.
    }
    return A;
}
static int compare(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

void SortArray(int *A, int N){
    qsort(A, N, sizeof(int), compare);
}


void DeallocateArray(int *A)
{
    free(A);

}

int main()
{
    int sizes[8] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000 };

/* For fun:
 *  int sizes[11] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000,
 *                    256000, 512000, 1024000 }; 
 */

    for (int i = 0 ; i < 8 ; i++)
    {
        double alloc_time = 0., sort_time = 0., dealloc_time = 0.;
        struct timeval startTime;
        struct timeval endTime;

        /* Call the three functions in a sequence. */

        gettimeofday(&startTime, NULL);
        int *arr = AllocateArray(sizes[i]); //reassigning it for easier use
        gettimeofday(&endTime, NULL);
        alloc_time = (endTime.tv_sec - startTime.tv_sec) * 1000.0 + (endTime.tv_usec - startTime.tv_usec) / 1000.0;


        gettimeofday(&startTime, NULL);
        SortArray(arr, sizes[i]); 
        gettimeofday(&endTime, NULL);
        sort_time = (endTime.tv_sec - startTime.tv_sec) * 1000.0 + (endTime.tv_usec - startTime.tv_usec) / 1000.0;


        gettimeofday(&startTime, NULL);
        DeallocateArray(arr);
        gettimeofday(&endTime, NULL);
        dealloc_time = (endTime.tv_sec - startTime.tv_sec) * 1000.0 + (endTime.tv_usec - startTime.tv_usec) / 1000.0;
        

        printf("Timings for array of size %d\n", sizes[i]);
        printf("\tTime for allocation is %g, time per element = %g\n", alloc_time, alloc_time/sizes[i]);
        printf("\tTime for sort_time is %g, time per element = %g\n", sort_time, sort_time/sizes[i]);
        printf("\tTime for deallocation is %g\n", dealloc_time);
    }
}
