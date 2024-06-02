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

|Group|Class|Description|
|-|-|------------|
|Dihedral|`D(sides = 3)`|D<sub>n</sub> is the group of symmetries of a regular polygon. See [1] below.|
|Addition modulo *n*|`Z(n = 1)`|*Z*<sub>n</sub> is the group {0, 1, ..., *n*-1} formed under addition modulo *n*.|
|Multiplication modulo *n*|`U(n = 1)`|*U*<sub>n</sub> is the group {1 <= *x* < *n* : gcd(*n*, *x*) = 1} formed under multiplication modulo *n*.|
|*K*<sub>4</sub>|`K4()`|Klein's 4 group.|
|*Q*<sub>8</sub>|`Q8()`|Quaternion group.|
|EDP|`EDP(G1, G2, ..., Gn)`|External Direct Product of groups.|

[1]	The `symmetries\dihedral.py` module implements the idea of polygon symmetries using permutations. A polygon is defined with the following characteristics:
- its number of sides;
- its state: the current order of its vertices;
- its symmetries: rotations union reflections.

Assuming the current state of a square is `[1, 2, 3, 4]`, then applying 2 unit rotations will make this current state into `[3, 4, 1, 2]`. Similarly other rotations and reflections can be applied.

**Nomenchlature.** The symmetries are named in a polygon as follows:
- rotations of *n* units: denoted by `n`;
- reflection about vertex at index *n*: denoted by `(n, )`;
- reflection about axis passing between vertices at index *n* and *n + 1*: denoted by `(n, n+1)`.

You can use that module to see how a polygon's vertices change upon applying various symmetries. Work will be continued on it.	∎

## Library Usage

#### Introduction

Import the library by running

```python
>>> from groups import *
```

and define a group:

```python
>>> D4 = D(4) # dihedral group of a square's symmetries
>>> D4
G({'r1', 'r0', 's0', 's3', 's2', 's1', 'r2', 'r3'})
```

Check the available members:

```python
>>> D4.members
{'r3', 's1', 'r2', 'r1', 's3', 'r0', 's2', 's0'}
```

#### Applying operations

Use the `apply()` method to apply an operation (or composition thereof) to the identity and see the output. Examples:

```python
>>> D4.apply("r1", "s2")
's3'
>>> D4.apply("s1", "s1") # reflection between vertices at indices 1 and 2, applied twice. |(1, 2)| = 2
'r0'
>>> U13 = U(13)
>>> U13.apply(3, 8) # 3 * 8 (mod 13)
11
```

or something more exciting:

```python
>>> D240 = D(240)
>>> D240.apply("r190", "s60", "r100", "s200")
'r190'
```

#### Forming EDPs

Form External Direct Products:

```python
>>> EDP1 = EDP(Z(12), U(20), Q8())
>>> len(EDP1) # = 12 * 8 * 8
768
```

and perform component wise operations

```python
>>> EDP1.apply((5, 3, "-j"), (8, 19, "k"))
(1, 17, 'i')
```

Beautiful!

#### Orders & Inverses

Find inverses or orders of group elements:

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

Printing table of orders and inverses:

```python
>>> D6 = D(6)
>>> print("x", "\t", "|x|", "\t", "x^(-1)")
... for x in D6:
...     print(x, "\t", D6.inverse(x), "\t", D6.order(x))
...
x 	 |x| 	 x^(-1)
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

#### Cayley Table

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

#### Subgroups

See a group's subgroups using `subgroups()` method:

```python
>>> D8 = D(8)
>>> D8_subs = D8.subgroups()
>>> for subgroup in sorted(d8_subs):
...     print(len(subgroup), "\t", subgroup)
...
1 	 {'r0'}
2 	 {'r0', 'r4'}
2 	 {'r0', 's0'}
2 	 {'r0', 's1'}
2 	 {'r0', 's2'}
2 	 {'r0', 's3'}
2 	 {'r0', 's4'}
2 	 {'r0', 's5'}
2 	 {'r0', 's6'}
2 	 {'r0', 's7'}
4 	 {'r0', 'r2', 'r6', 'r4'}
4 	 {'r0', 's0', 's4', 'r4'}
4 	 {'r0', 's1', 's5', 'r4'}
4 	 {'r0', 's2', 'r4', 's6'}
4 	 {'r0', 's3', 's7', 'r4'}
8 	 {'r5', 'r1', 'r0', 'r4', 'r7', 'r2', 'r6', 'r3'}
8 	 {'r0', 's0', 'r4', 's2', 'r2', 'r6', 's4', 's6'}
8 	 {'r0', 's3', 'r4', 's1', 'r2', 'r6', 's5', 's7'}
16 	 {'r5', 'r1', 's7', 'r0', 's0', 's3', 'r4', 's2', 's1', 'r7', 'r2', 'r6', 'r3', 's4', 's5', 's6'}
```

List the cyclic subgroups of U<sub>30</sub> (see [this](https://math.stackexchange.com/questions/3390079/systematically-list-the-cyclic-subgroups-of-u30)):

```python
>>> U30s = U(30).subgroups()
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
>>> for subgroup in EDP(Z(4), U(8)).subgroups(order = 4):
... 	print(subgroup)
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
>>> len(EDP(K4(), K4()).subgroups())
67
```

Check a certain set is a subgroup or not using `check_subgroup()`:

```python
>>> D(8).check_subgroup({"r0"})
True
>>> U(10).check_subgroup({3, 7})
False
```

Subgroups generated by elements:

```python
>>> Z(30).generate(4)
G({0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28})
```

Get Factor Groups:

```python
>>> 

####  Subgroups: Normal

Get cosets generated by elements:

```python
>>> e = EDP(U(8), K4())
>>> s = e.subgroups()[3] # get any subgroup
>>> e.coset(s, (3, "b")) # (left) coset of element (3, "b") in subgroup s
{(3, 'a'), (3, 'b')}
>>> e.coset(s, (3, "b"), "r")
{(3, 'b'), (3, 'a')} # right coset
```

Normal subgroups of a group:

```python
>>> for i in D(5).nsubgroups():
...     print(i)
...
{'r0'}
{'r1', 'r0', 'r4', 'r2', 'r3'}
{'r1', 'r0', 's0', 's3', 'r4', 's2', 's1', 'r2', 'r3', 's4'}
```

#### Custom defined groups

If you wish to expand and implement a group structure yourself, see `groups\definitions\definition_template.py`.

... and that is not all! Countless other things are possible if we are innovative enough. Thank you for reading this far.