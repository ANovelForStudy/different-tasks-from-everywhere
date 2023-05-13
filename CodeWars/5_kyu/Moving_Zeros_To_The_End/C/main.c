
#include <stdio.h>
#include "test.h"

int main() {
    
    int arr[] = {1, 0, 1, 2, 0, 1, 3};
    int length = 7;

    printf("Before : ");
    for (int i = 0; i < length; ++i) {
        printf("%d ", *(arr+i));
    }
    printf("\n");

    move_zeros(length, arr);

    printf("After : ");
    for (int i = 0; i < length; ++i) {
        printf("%d ", *(arr+i));
    }
    printf("\n");

    return 0;
}

