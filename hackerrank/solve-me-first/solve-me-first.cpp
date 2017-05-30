#include <iostream>

int
solve_me_first(int a, int b) {
    return a + b;
}

int
main() {
    int num1, num2;
    std::cin >> num1 >> num2;
    int sum = solve_me_first(num1, num2);
    std::cout << sum << std::endl;
    return 0;
}
