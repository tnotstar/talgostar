Roman numerals
==============

Source
------

This document has been stolen from <https://py.checkio.org/mission/roman-numerals/>

Synopsis
--------

Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

> I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:

 Symbol | Value
--------+-------
    I   | 1 (unus)
    V   | 5 (quinque)
    X   | 10 (decem)
    L   | 50 (quinquaginta)
    C   | 100 (centum)
    D   | 500 (quingenti)
    M   | 1.000 (mille)

More additional information about roman numerals can be found on the [Wikipedia article].

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input
-----

A number as an integer.

Output
------

The Roman numeral as a string.

Example
-------

~~~~
checkio(6) == "VI"
checkio(76) == "LXXVI"
checkio(13) == "XIII"
checkio(44) == "XLIV"
checkio(3999) == "MMMCMXCIX"
~~~~

How it is used
--------------

This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation. The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world and you read about it [here]. Or maybe you will have a customer from Ancient Rome ;-)

Precondition(s)
---------------

  * `0 < number < 4000`

[Wikipedia article]: https://en.wikipedia.org/wiki/Roman_numerals "Roman numerals"
[here]: https://en.wikipedia.org/wiki/Roman_numerals#Modern_use "Roman numerals ― Modern use"

