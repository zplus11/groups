
# groups

## Introduction

**Definition** *(Group)*. A group is a non-empty set in Mathematics, elements of which follow 4 properties namely Closure, Associativity, Existence of Identity and Existence of Inverses under a certain operation.

Study group structures easily with python! This library contains various modules related to select group structures in Mathematics, some being `dihedral.py`, `z.py`, `edp.py`, and more. This is a work in continuous progress, and I hope to continue working on this and add many more groups gradually. This README file walks you through the available modules.

## Installation
To install the library, run

```
pip install git+"https://github.com/zplus11/groups"
```

## Available Groups

### Dihedral group

**Definition** *(Dihedral group)*. A dihedral group of order 2*n* is the set of all "symmetries" of a regular polygon with *n* sides forming a group under their composition.

The `dihedral.py` module implements the idea of dihedral groups using permutations. A polygon is defined with the following characteristics:
- its number of sides;
- its state: the current order of its vertices;
- its symmetries: rotations union reflections.

Assuming the current state of a square is `[1, 2, 3, 4]`, then applying 2 unit rotations will make this current state into `[3, 4, 1, 2]`. Similarly other rotations and reflections can be applied.

**Nomenchlature.** The symmetries are named in a polygon as follows:
- rotations of *n* units: denoted by `n`;
- reflection about vertex at index *n*: denoted by `(n, )`;
- reflection about axis passing between vertices at index *n* and *n + 1*: denoted by `(n, n+1)`.

### Addition modulo *n*

**Definition** *(Z_n)*. *Z_n* is the set {0, 1, ..., n-1} forming a group under addition modulo *n*.

### Multiplication modulo *p*

**Definition** *(U_n)*. *U_n* is the set {1 <= x < n: gcd(n, x) = 1} forming a group under multiplication modulo *n*.

### External Direct Products

**Definition** *(EDP)*. An EDP (External Direct Product) is a cross product of two or more groups forming another group under component wise operation.


## Library Usage

Import the library by running

```
>>> from groups import *
```

and define a group:

```
>>> d4 = dihedral(sides = 4) # dihedral group of a square's symmetries
```

Check the available members:

```
>>> d4.members
[0, 1, 2, 3, (0,), (1,), (0, 1), (1, 2)]
```

Use the `apply()` method to apply an operation (or composition thereof) to the identity and see the output. Examples:

```
>>> d4.apply(1) # 1 unit rotation
[4, 1, 2, 3]

>>> d4.apply(1, (0, )) # reflection about axis passing through vertex at 0 index, then a unit rotation
[4, 3, 2, 1]

>>> d4.apply((1, 2), (1, 2)) # reflection between vertices at indices 1 and 2, applied twice. |(1, 2)| = 2
[1, 2, 3, 4]

>>> u13 = u(13)
>>> u13.apply(3, 8) # 3 * 8 (mod 13)
11
```

and so on. Determine the composition of operations as follows:

```
>>> d3 = dihedral() # default sides = 3
>>> my_sym = d3.apply(2, (0, ))
>>> d3.determine(my_sym)
(2,)
```

or something more exciting:

```
>>> d24 = dihedral(24)
>>> d24.determine(d24.apply((8, 9), 12, (7, ), (11, 12), 3))
(8, 9)
```

Form EDP's:

```
>>> edp1 = edp(d24, u13)
>>> len(edp1.members) # this will be len(d24.members)*len(u13.members). 48 times 10 is indeed 480.
480
```

and perform component wise operations

```
>>> edp1.apply((2, 3), ((1, ), 2))
([5, 4, 3, 2, 1, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6], 6)
```

Beautiful! Find inverses or orders of group elements:

```
>>> d24.inverse(element = 13) # inverse of element "13" in d24
11
>>> edp1.inverse(element = ((5, ), 5))
((5,), 8)
<<<<<<< HEAD
>>> u(1000).order(883)
100
>>> d24.order((7, 8))
2
```

See a group's subgroups using `subgroups()` method:

```
>>> d8 = dihedral(8)
>>> d8_subs = d8.subgroups()
>>> for subgroup in sorted(d8_subs, key = len):
...     print(len(subgroup), "\t", subgroup)
...
1        [0]
2        [0, 4]
2        [0, (0,)]
2        [0, (1,)]
2        [0, (2,)]
2        [0, (3,)]
2        [0, (0, 1)]
2        [0, (1, 2)]
2        [0, (2, 3)]
2        [0, (3, 4)]
4        [0, 2, 4, 6]
4        [0, 4, (0,), (2,)]
4        [0, 4, (1,), (3,)]
4        [0, 4, (0, 1), (2, 3)]
4        [0, 4, (1, 2), (3, 4)]
8        [0, 1, 2, 3, 4, 5, 6, 7]
8        [0, 2, 4, 6, (0,), (1,), (2,), (3,)]
8        [0, 2, 4, 6, (0, 1), (1, 2), (2, 3), (3, 4)]
16       [0, 1, 2, 3, 4, 5, 6, 7, (0,), (1,), (2,), (3,), (0, 1), (1, 2), (2, 3), (3, 4)]
>>> [print(subgroup) for subgroup in edp(z(4), u(8)).subgroups(4)]
...
[(0, 1), (0, 3), (0, 5), (0, 7)]
[(0, 1), (0, 3), (2, 1), (2, 3)]
[(0, 1), (0, 3), (2, 5), (2, 7)]
[(0, 1), (0, 5), (2, 1), (2, 5)]
[(0, 1), (0, 5), (2, 3), (2, 7)]
[(0, 1), (0, 7), (2, 1), (2, 7)]
[(0, 1), (0, 7), (2, 3), (2, 5)]
[(0, 1), (1, 1), (2, 1), (3, 1)]
[(0, 1), (1, 3), (2, 1), (3, 3)]
[(0, 1), (1, 5), (2, 1), (3, 5)]
[(0, 1), (1, 7), (2, 1), (3, 7)]
```

Or check a certain set is a subgroup or not using `check_subgroup()`:

```
>>> d8.check_subgroup([0])
True
>>> d8.check_subgroup([0, (0, )])
True
>>> d8.check_subgroup([(0,), (1,), (0, 1)])
False
```

Thank you for reading this far!
