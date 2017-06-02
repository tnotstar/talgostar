#include <stdlib.h>
#include <stdio.h>

int
simple_array_sum (int *data, int n) {
    int sum, i;
    for (sum = 0, i = 0; i < n; i++)
        sum += data[i];
    return sum;
}

int
main () {
    int *data, n, i;

    scanf("%d", &n);
    if (n <= 0)
        return -1;
    data = malloc(sizeof(int) * n);
    if (!data)
        return -2;
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);

    printf("%d\n", simple_array_sum(data, n));
    free(data);

    return 0;
}
