#include <iostream>

using namespace std;

int main(void)
{
    int N;
    cin >> N;

    int i, numArray[N];      // Define an array of four integers

    // Get inputs for the array elements
    for (i = 0; i < N; i++) {
        cin >> numArray[i];
    }

    // Write here the logic to add these integers:
    int sum = 0;
    for (i = 0; i < N; i++) {
        sum += numArray[i];
    }
    cout << sum << endl;     // Print the sum

    return 0;
}