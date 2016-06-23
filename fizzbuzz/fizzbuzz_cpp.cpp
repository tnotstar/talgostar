#include <iostream>

using namespace std;

int
main () {
    for (int n = 1; n <= 100; n++) {
        if (n % 15 == 0)
            cout << "fizzbuzz" << endl;
        else if (n % 5 == 0)
            cout << "buzz" << endl;
        else if (n % 3 == 0)
            cout << "fizz" << endl;
        else
            cout << n << endl;
    }
    return 0;
}

/* EOF */
