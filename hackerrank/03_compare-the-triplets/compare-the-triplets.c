#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int first, second;
} pair;

pair
compare_the_triplets(int *a, int *b, int n) {
    pair rs = {0, 0};
    for(int i = 0; i < n; i++) {
        if(a[i] > b[i])
            rs.first++;
        else if(a[i] < b[i])
            rs.second++;
    }
    return rs;
}

int
main () {
    int i, a[3], b[3];

    for(i = 0; i < 3; ++i)
        scanf("%d", &a[i]);
    for(i = 0; i < 3; ++i)
        scanf("%d", &b[i]);

    pair rs = compare_the_triplets(a, b, 3  );
    printf("%d %d", rs.first, rs.second);

    return 0;
}
