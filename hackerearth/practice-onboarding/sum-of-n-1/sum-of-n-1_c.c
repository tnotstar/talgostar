#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int i, numArray[N];      // Define an array of four integers

    // Get inputs for the array elements
    for (i = 0; i < N; i++) {
        scanf("%d", &numArray[i]);
    }

    // Write here the logic to add these integers:
    int sum = 0;
    for (i = 0; i < N; i++) {
        sum += numArray[i];
    }
    printf("%d\n",sum);      // Print the sum

    return 0;
}