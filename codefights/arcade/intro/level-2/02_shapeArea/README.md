Shape Area
==========

Source
------

This document has been stolen from <https://codefights.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ>

Problem
-------

Below we will define an `n`-interesting polygon. Your task is to find the area of a polygon for a given `n`.

A `1`-interesting polygon is just a square with a side of length `1`. An `n`-interesting polygon is obtained by taking the `n - 1`-interesting polygon and appending `1`-interesting polygons to its rim, side by side. You can see the `1-`, `2-`, `3-` and `4-`interesting polygons in the picture below.

```
  |  |  |  |  |  |  |  |  |  |  |  |
--+--+--+--+--+--+--+--+--+--+--+--+--
  |  |  |  |  |  |  |  |  |XX|  |  |
--+--+--+--+--+--+--+--+--+--+--+--+--
  |  |  |  |XX|  |  |  |XX|XX|XX|  |
--+--+--+--+--+--+--+--+--+--+--+--+--
  |XX|  |XX|XX|XX|  |XX|XX|XX|XX|XX|
--+--+--+--+--+--+--+--+--+--+--+--+--
  |  |  |  |XX|  |  |  |XX|XX|XX|  |
--+--+--+--+--+--+--+--+--+--+--+--+--
  |  |  |  |  |  |  |  |  |XX|  |  |
--+--+--+--+--+--+--+--+--+--+--+--+--
  |  |  |  |  |  |  |  |  |  |  |  |
  n = 1    n = 2          n = 3
```

Example
-------

  * For `n = 1`, the output should be `shapeArea(n) = 1`,
  * For `n = 2`, the output should be `shapeArea(n) = 5`, &
  * For `n = 3`, the output should be `shapeArea(n) = 13`.

Input/Output
------------

  * \[input\] `integer n`

    An array of integers containing at least two elements.

    Guaranteed constraints:

      * 1 ≤ n ≤ 10^4.

  * \[output\] `integer`

    The area of the `n`-interesting polygon.
