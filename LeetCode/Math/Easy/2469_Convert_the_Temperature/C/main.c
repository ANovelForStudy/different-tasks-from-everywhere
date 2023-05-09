
#include <stdio.h>
#include <stdlib.h>


double* convertTemperature(double celsius, int* returnSize){
    double* result = malloc(sizeof(double) * 2);
    *result = celsius + 273.15; 
    *(result+1) = celsius * 1.8 + 32;
    *(returnSize) = 2;
    return result;
}


int main(int argc, char const *argv[])
{
    int size;
    double* result = convertTemperature(36.5, &size);

    printf("Kelvin: %lf Fahrenheit: %lf\n", *(result), *(result+1));

    return 0;
}

