# groups v1.4.0

## Introduction

`groups` is a basic Computer Algebra System to study various finite group structures from Group Theory.

**Definition** *(Group)*. A group is a non-empty set in Mathematics, elements of which follow 4 properties namely Closure, Associativity, Existence of Identity and Existence of Inverses under a certain operation.

Study finite group structures easily with python! This library contains various modules related to select group structures in Mathematics, some being `dihedral.py`, `z.py`, `edp.py`, and more. This is a work in continuous progress, and I hope to continue working on this and add many more groups gradually. This README file walks you through the available modules.

## Installation

To install the library, run

```
pip install git+"https://github.com/zplus11/groups"
```

## Available Groups

`groups` offers the following Groups:

|Group|Class|Identity|Description|
|-|-|-|------------|
|Dihedral|`dihedral(sides = 3)`|`0`|D<sub>n</sub> is the group of symmetries of a regular polygon. Polygon images (order of vertices) are stored in list forms, such as a square would be `[1, 2, 3, 4]` and these lists are manipulated upon application of symmetrie. See [1] below.|
|Addition modulo *n*|`z(n = 1)`|`0`|*Z*<sub>n</sub> is the group {0, 1, ..., *n*-1} formed under addition modulo *n*.|
|Multiplication modulo *n*|`u(n = 1)`|`1`|*U*<sub>n</sub> is the group {1 <= *x* < *n* : gcd(*n*, *x*) = 1} formed under multiplication modulo *n*.|
|*K*<sub>4</sub>|`k4()`|`"e"`|Klein's 4 group.|
|*Q*<sub>8</sub>|`q8()`|`"1"`|Quaternion group.|
|EDP|`edp(g1(), g2(), ..., gn())`|Identity tuple|External Direct Product of groups.|

<sup>[1]</sup>The `dihedral.py` module implements the idea of dihedral groups using permutations. A polygon is defined with the following characteristics:
- its number of sides;
- its state: the current order of its vertices;
- its symmetries: rotations union reflections.

Assuming the current state of a square is `[1, 2, 3, 4]`, then applying 2 unit rotations will make this current state into `[3, 4, 1, 2]`. Similarly other rotations and reflections can be applied.

**Nomenchlature.** The symmetries are named in a polygon as follows:
- rotations of *n* units: denoted by `n`;
- reflection about vertex at index *n*: denoted by `(n, )`;
- reflection about axis passing between vertices at index *n* and *n + 1*: denoted by `(n, n+1)`. ∎

## Library Usage

#### Introduction

Import the library by running

```python
>>> from groups import *
```

and define a group:

```python
>>> d4 = dihedral(sides = 4) # dihedral group of a square's symmetries
```

Check the available members:

```python
>>> d4.members
[0, 1, 2, 3, (0,), (1,), (0, 1), (1, 2)]
```

#### Applying operations

Use the `apply()` method to apply an operation (or composition thereof) to the identity and see the output. Examples:

```python
>>> d4.apply(1) # 1 unit rotation
[4, 1, 2, 3]
>>> d4.apply(1, (0, )) # reflection about axis passing through vertex at 0 index, then a unit rotation
[2, 1, 4, 3]
>>> d4.apply((1, 2), (1, 2)) # reflection between vertices at indices 1 and 2, applied twice. |(1, 2)| = 2
[1, 2, 3, 4]
>>> u13 = u(13)
>>> u13.apply(3, 8) # 3 * 8 (mod 13)
11
```

and so on. Determine the composition of operations as follows:

```python
>>> u10 = u(10)
>>> composed = u10.apply(3, 7)
>>> u10.determine(composed)
1
```

or something more exciting:

```python
>>> d24 = dihedral(24)
>>> d24.determine(d24.apply((8, 9), 12, (7, ), (11, 12), 3))
(5, 6)
```

#### Forming EDPs

Form External Direct Products:

```python
>>> edp1 = edp(z(12), u(20), q8())
>>> len(edp1.members) # = 12 * 8 * 8
768
```

and perform component wise operations

```python
>>> edp1.apply((5, 3, "-j"), (8, 19, "k"))
(1, 17, 'i')
```

Beautiful!

#### Orders & Inverses

Find inverses or orders of group elements:

```python
>>> dihedral(24).inverse(element = 13) # inverse of element "13" in d24
11
>>> edp1.inverse(element = (5, 7, "-i"))
(7, 3, 'i')
>>> u(1000).order(883)
100
>>> dihedral(20).order((7, 8))
2
```

Printing table of orders and inverses:

```python
>>> d6 = dihedral(6)
>>> print("x", "\t", "|x|", "\t", "x^(-1)")
... for i in d6.members:
...     print(i, "\t", d6.order(i), "\t", d6.inverse(i))
...
"x"	"|x|"	"x^(-1)"
0        1       0
1        6       5
2        3       4
3        2       3
4        3       2
5        6       1
(0,)     2       (0,)
(1,)     2       (1,)
(2,)     2       (2,)
(0, 1)   2       (0, 1)
(1, 2)   2       (1, 2)
(2, 3)   2       (2, 3)
```

#### Cayley Table

```python
>>> q8().cayley()
0 = 1
1 = -1
2 = i
3 = -i
4 = j
5 = -j
6 = k
7 = -k
----------------------------------
   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7

0  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
1  | 1 | 0 | 3 | 2 | 5 | 4 | 7 | 6
2  | 2 | 3 | 1 | 0 | 7 | 6 | 4 | 5
3  | 3 | 2 | 0 | 1 | 6 | 7 | 5 | 4
4  | 4 | 5 | 6 | 7 | 1 | 0 | 3 | 2
5  | 5 | 4 | 7 | 6 | 0 | 1 | 2 | 3
6  | 6 | 7 | 5 | 4 | 2 | 3 | 1 | 0
7  | 7 | 6 | 4 | 5 | 3 | 2 | 0 | 1
```

#### Subgroups

See a group's subgroups using `subgroups()` method:

```python
>>> d8 = dihedral(8)
>>> d8_subs = d8.subgroups()
>>> for subgroup in sorted(d8_subs, key = len):
...     print(len(subgroup), "\t", subgroup)
...
1        {0}
2        {0, 4}
2        {0, (0,)}
2        {0, (1,)}
2        {0, (2,)}
2        {0, (3,)}
2        {0, (0, 1)}
2        {0, (1, 2)}
2        {0, (2, 3)}
2        {0, (3, 4)}
4        {0, 2, 4, 6}
4        {0, (0,), 4, (2,)}
4        {0, (1,), (3,), 4}
4        {0, (2, 3), 4, (0, 1)}
4        {0, (1, 2), 4, (3, 4)}
8        {0, 1, 2, 3, 4, 5, 6, 7}
8        {0, 2, (2,), 4, 6, (1,), (0,), (3,)}
8        {0, (0, 1), 2, (1, 2), 4, (3, 4), 6, (2, 3)}
16       {0, 1, 2, 3, 4, 5, 6, 7, (2,), (0, 1), (1, 2), (3, 4), (2, 3), (1,), (0,), (3,)}
```

List the cyclic subgroups of U<sub>30</sub> (see [this](https://math.stackexchange.com/questions/3390079/systematically-list-the-cyclic-subgroups-of-u30)):

```python
>>> u30s = u(30).subgroups()
>>> for i in u30s:
...     if u(30).cyclic(i): print(i)
...
{1}
{1, 11}
{1, 19}
{1, 29}
{1, 19, 13, 7}
{1, 19, 17, 23}
```

Find subgroups of certain order:

```python
>>> [print(subgroup) for subgroup in edp(z(4), u(8)).subgroups(order = 4)]
...
{(0, 1), (0, 7), (0, 3), (0, 5)}
{(0, 1), (0, 3), (2, 3), (2, 1)}
{(0, 1), (0, 3), (2, 5), (2, 7)}
{(0, 1), (2, 5), (2, 1), (0, 5)}
{(0, 1), (2, 3), (2, 7), (0, 5)}
{(0, 1), (0, 7), (2, 1), (2, 7)}
{(0, 1), (0, 7), (2, 5), (2, 3)}
{(0, 1), (3, 1), (1, 1), (2, 1)}
{(0, 1), (3, 3), (1, 3), (2, 1)}
{(0, 1), (2, 1), (3, 5), (1, 5)}
{(0, 1), (3, 7), (1, 7), (2, 1)}
```

Subgroups of EDP of `k4()` and `k4()`:

```python
>>> len(edp(k4(), k4()).subgroups())
67
```

Check a certain set is a subgroup or not using `check_subgroup()`:

```python
>>> dihedral(8).check_subgroup([0])
True
>>> u(10).check_subgroup([3, 7])
False
```

####  Subgroups: Normal

Get cosets generated by elements:

```python
>>> e = edp(u(8), k4())
>>> s = e.subgroups()[3] # get any subgroup
>>> e.coset(s, (3, "b")) # (left) coset of element (3, "b") in subgroup s
{(3, 'a'), (3, 'b')}
>>> e.coset(s, (3, "b"), "r")
{(3, 'b'), (3, 'a')} # right coset
```

Normal subgroups of a group:

```python
>>> for i in dihedral(5).nsubgroups():
...     print(i)
...
{0}
{0, 1, 2, 3, 4}
{0, 1, 2, 3, 4, (2,), (4,), (1,), (0,), (3,)}
```

#### Custom defined groups

If you wish to expand and implement a group structure yourself, see `groups\definitions\definition_template.py`.

... and that is not all! Countless other things are possible if we are innovative enough. Thank you for reading this far.