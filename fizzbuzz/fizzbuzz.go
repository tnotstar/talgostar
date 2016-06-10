//usr/bin/env go run "$0" "$@"; exit "$?"

package main

import "fmt"

func main() {
    for n := 1; n < 101; n++ {
        if n % 15 == 0 {
            fmt.Println("fizzbuzz");
        } else if n % 5 == 0 {
            fmt.Println("buzz");
        } else if n % 3 == 0 {
            fmt.Println("fizz");
        } else {
            fmt.Println(n);
        }
    }
}

// EOF
