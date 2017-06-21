#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checkPalindrome(inputString):
    los = len(inputString)
    for i in range(los // 2):
        if inputString[i] != inputString[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    assert checkPalindrome("aabaa"), "Test #1"
    assert not checkPalindrome("abac"), "Test #2"
    assert checkPalindrome("a"), "Test #3"
    assert not checkPalindrome("az"), "Test #4"
    assert checkPalindrome("abacaba"), "Test #5"
    assert checkPalindrome("z"), "Test #6"
    assert not checkPalindrome("aaabaaaa"), "Test #7"
    assert not checkPalindrome("zzzazzazz"), "Test #8"
    assert checkPalindrome("hlbeeykoqqqqokyeeblh"), "Test #9"
    assert checkPalindrome("hlbeeykoqqqokyeeblh"), "Test #10"

# EOF