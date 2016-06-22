#include <stdio.h>

int
main (void) {
    for (int n = 1; n <= 100; n++) {
        if (n % 15 == 0)
            printf("fizzbuzz\n");
        else if (n % 5 == 0)
            printf("buzz\n");
        else if (n % 3 == 0)
            printf("fizz\n");
        else
            printf("%d\n", n);
    }
    return 0;
}

/* EOF */
