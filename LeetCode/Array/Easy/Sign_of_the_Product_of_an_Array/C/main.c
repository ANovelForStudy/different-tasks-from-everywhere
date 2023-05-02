#include <stdio.h>

char arraySign(int* nums, unsigned short numsSize){
    char neg = 1;
    for (unsigned short i = 0; i < numsSize; i++) {       
        if (nums[i] == 0) return 0;
        if (nums[i] < 0) neg = -neg;
    }
    return neg;
}