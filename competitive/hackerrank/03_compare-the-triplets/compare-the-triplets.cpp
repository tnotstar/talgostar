#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

template <class T>
std::pair<T, T>
compare_the_triplets(std::vector<T> &a, std::vector<T> &b) {
    typename std::vector<T>::iterator it_a = a.begin(), it_b = b.begin();
    T counter_a = 0, counter_b = 0;
    for(/* void */; it_a != a.end() && it_b != b.end(); ++it_a, ++it_b) {
        if(*it_a > *it_b)
            ++counter_a;
        else if(*it_a < *it_b)
            ++counter_b;
    }
    return std::make_pair(counter_a, counter_b);
}

int
main() {
    std::vector<int> a;
    std::copy_n(std::istream_iterator<int>(std::cin), 3, std::back_inserter(a));

    std::vector<int> b;
    std::copy_n(std::istream_iterator<int>(std::cin), 3, std::back_inserter(b));

    std::pair<int, int> rs = compare_the_triplets(a, b);
    std::cout << rs.first << " " << rs.second << std::endl;

    return 0;
}
