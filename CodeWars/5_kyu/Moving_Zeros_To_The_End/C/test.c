
#include <stddef.h>
#include <stdlib.h>
#include "test.h"

void move_zeros(size_t len, int arr[len])
{
    int temp;
    for (short i = 0; i < len; i++) {
        if (*(arr+i) == 0) {
            for (short j = i + 1; j < len; j++) {
                if (j == len)
                  return;
                
                if (*(arr+j) != 0) {
                    *(arr+i) = *(arr+j);
                    *(arr+j) = 0;
                    break;
                }
            }
        }
    }
}
