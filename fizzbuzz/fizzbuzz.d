#!/usr/bin/env rdmd

import std.stdio;

void main() {
    foreach (n; 1 .. 101) {
        if (n % 15 == 0)
            writeln("fizzbuzz");
        else if (n % 5 == 0)
            writeln("buzz");
        else if (n % 3 == 0)
            writeln("fizz");
        else
            writeln(n);
    }
}

// EOF
