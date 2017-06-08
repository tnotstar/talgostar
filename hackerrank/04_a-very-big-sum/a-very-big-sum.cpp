#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <numeric>

template <typename T>
T
a_very_big_sum(std::vector<T> const &a) {
    return std::accumulate(a.begin(), a.end(), 0LL);
}

typedef long long int long_long_t;

int
main() {
    int n;
    std::cin >> n;

    std::vector<long_long_t> a;
    std::copy_n(std::istream_iterator<int>(std::cin), n, std::back_inserter(a));

    std::cout << a_very_big_sum<long_long_t>(a) << std::endl;

    return 0;
}
