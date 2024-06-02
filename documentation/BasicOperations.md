
[Next - Subgroups](Subgroups.md)

[Previous - Introduction](Introduction.md)

### Basic Operations

Define a group using one of the classes as follows:

```python
>>> D4 = D(4) # Dihedral group of order 2*4
>>> D4
G({'r1', 'r0', 's0', 's3', 's2', 's1', 'r2', 'r3'})
```

and check the available members:

```python
>>> len(D4)
8
>>> D4.members
{'r3', 's1', 'r2', 'r1', 's3', 'r0', 's2', 's0'}
```

Group operations can be applied using the `apply()` method available for each group object. For example, we can find what is r0*s2 by typing

```python
>>> D4.apply("r0", "s2")
's2'
>>> # More examples
>>> D4.apply("s1", "s1") # reflection between vertices at indices 1 and 2, applied twice. |(1, 2)| = 2
'r0'
>>> U13 = U(13) # Multiplicative group of integers modulo n
>>> U13.apply(3, 4, 2) # 3 * 4 * 2 (mod 13)
11
```

or do something more exciting:

```python
>>> D240 = D(240)
>>> D240.apply("r190", "s60", "r100", "s200")
'r190'
```

External Direct Products of various groups can be formed as follows:

```python
>>> EDP1 = EDP(Z(12), U(20), Q8())
>>> len(EDP1) # = 12 * 8 * 8
768
```

where `Q8()` is the Qaternions group. `apply()` in EDPs is operated component wise in the tuples.

```python
>>> EDP1.apply((5, 3, "-j"), (8, 19, "k"))
(1, 17, 'i')
```

#### Cayley Tables

A complete Cayley table can be printed with the `cayley()` method for every group. For example:

```python
>>> Q8().cayley()
0 = -1
1 = -i
2 = -j
3 = -k
4 = 1
5 = i
6 = j
7 = k
----------------------------------
     0   1   2   3   4   5   6   7

0    4 | 5 | 6 | 7 | 0 | 1 | 2 | 3
1    5 | 0 | 3 | 6 | 1 | 4 | 7 | 2
2    6 | 7 | 0 | 1 | 2 | 3 | 4 | 5
3    7 | 2 | 5 | 0 | 3 | 6 | 1 | 4
4    0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
5    1 | 4 | 7 | 2 | 5 | 0 | 3 | 6
6    2 | 3 | 4 | 5 | 6 | 7 | 0 | 1
7    3 | 6 | 1 | 4 | 7 | 2 | 5 | 0
```

#### Orders and Inverses

Orders and inverses can be found using `order()` and `inverse()` methods respectively.

```python
>>> D(24).inverse(element = "r13") # inverse of element "13" in d24
11
>>> EDP1.inverse(element = (5, 7, "-i"))
(7, 3, 'i')
>>> U(1000).order(883)
100
>>> dihedral(20).order("s7")
2
```

One step further, the complete table of these can also be printed.

```python
>>> D6 = D(6)
>>> print("x", "\t", "x^(-1)", "\t", "|x|")
... for x in D6:
...     print(x, "\t", D6.inverse(x), "\t", D6.order(x))
...
x 	 x^(-1)  |x|
r0 	 r0 	 1
r1 	 r5 	 6
r2 	 r4 	 3
r3 	 r3 	 2
r4 	 r2 	 3
r5 	 r1 	 6
s0 	 s0 	 2
s1 	 s1 	 2
s2 	 s2 	 2
s3 	 s3 	 2
s4 	 s4 	 2
s5 	 s5 	 2
```

<br>

[Next - Subgroups](Subgroups.md)

[Previous - Introduction](Introduction.md)