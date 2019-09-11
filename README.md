# nextprod.py

A pure-Python direct port of Julia's [nextprod](https://docs.julialang.org/en/v1/base/math/#Base.nextprod). Very useful when you want to pick FFT lengths with small prime factors, and much more.

**API** `def nextprod(a: List[int], x: int) -> int` returns the next integer greater than or equal to `x` that can be written as `math.prod(a)`.

**Installation** `$ pip install nextprod`

**Usage**
```py
from nextprod import nextprod
nextprod([2, 3, 5, 7], 1123)
```