#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <numeric>

template <class T>
T simple_array_sum(std::vector<T> &data) {
    return std::accumulate(data.begin(), data.end(), 0);
}

typedef std::vector<int> int_array;

int
main() {
    int n;
    std::cin >> n;

    std::vector<int> data;
    std::copy_n(std::istream_iterator<int>(std::cin), n, std::back_inserter(data));
    std::cout << simple_array_sum(data) << std::endl;

    return 0;
}
