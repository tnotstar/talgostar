All the Same
============

Source
------

This document has been stolen from <https://py.checkio.org/mission/all-the-same/>

Synopsis
--------

In this mission you should check if all elements in the given list are equal.

Input
-----

A List object.

Output
------

A Bool equals True if all list items are equals. Otherwise, False.

Example
-------

~~~~
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True
~~~~

> **Note:** The idea for this mission was found on [Python Tricks series by Dan Bader].

[Python Tricks series by Dan Bader]: https://dbader.org

How it is used
--------------

This concept can be useful if you need to parse config files and simplify structures for grandfathered systems and file structures. You can easily modify this idea for your own specifications. Besides that, it's a useful skill to be able to read code and search for bugs.

Precondition(s)
---------------

  * Precondition: all elements of the input list are hashable.
