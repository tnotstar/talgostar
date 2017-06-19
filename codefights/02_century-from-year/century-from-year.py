#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def centuryFromYear(year):
    return year // 100 + (year % 100 > 0)

if __name__ == "__main__":
    assert centuryFromYear(1905) == 20, "Test #1"
    assert centuryFromYear(1700) == 17, "Test #2"
    assert centuryFromYear(1988) == 20, "Test #3"
    assert centuryFromYear(2000) == 20, "Test #4"
    assert centuryFromYear(2001) == 21, "Test #5"
    assert centuryFromYear(200) == 2, "Test #6"
    assert centuryFromYear(374) == 4, "Test #7"

# EOF