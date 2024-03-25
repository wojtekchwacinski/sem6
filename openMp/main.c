#include <stdio.h>
#include <omp.h>

int main(){
#pragma omp parallel 
    for (int i = 0; i < 10; i++){
        int x = omp_get_thread_num();
        printf("%i, %i\n", i, x);
    }
    return 0;
}