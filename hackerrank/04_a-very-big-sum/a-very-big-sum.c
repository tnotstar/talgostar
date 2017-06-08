#include <stdlib.h>
#include <stdio.h>

typedef long long int long_long_t;

long_long_t
a_very_big_sum(long_long_t *A, int N) {
    long_long_t sum = 0;
    for(int i = 0; i < N; ++i)
        sum += A[i];
    return sum;
}

int
main () {
    long_long_t *A;
    int i, N;

    scanf("%d", &N);
    A = malloc(sizeof(long_long_t) * N);
    if(!A) {
        perror("oops: can't alloc memory for A");
        return -1;
    }

    for(i = 0; i < N; ++i)
        scanf("%lld", &A[i]);

    printf("%lld", a_very_big_sum(A, N));
    free(A);

    return 0;
}
