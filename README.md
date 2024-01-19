# symmetries

## Introduction

Study dihedral group structure easily with python using permutations!

**Definition** *(Dihedral group)*. A dihedral group of order 2*n* is the set of all "symmetries" of a regular polygon with *n* sides forming a group under their composition.

This python library implements the idea of dihedral groups using permutations. A polygon is defined with the following characteristics:
- its number of sides;
- its state: the current order of its vertices;
- its symmetries: rotations union reflections.

Assuming the current state of a square is `[1, 2, 3, 4]`, then applying 2 unit rotations will make this current state into `[3, 4, 1, 2]`. Similarly other rotations and reflections can be applied.

## Nomenchlature

The symmetries are defined in a polygon as follows:
- rotations of *n* units: denoted by `n`;
- reflection about vertex at index *n*: denoted by `(n, )`;
- reflection about axis passing between vertices at index *n* and *n + 1*: denoted by `(n, n+1)`.

## Usage

Import the library and define a dihedral group by

```
>>> from symmetries import *

>>> d4 = dihedral(sides = 4) # dihedral group of a square's symmetries
```

Use the `apply()` method to apply a symmetry to the square and determine its final state. Examples:

```
>>> d4.apply(1) # 1 unit rotation
[4, 1, 2, 3]

>>> d4.apply(1, (0, )) # reflection about axis passing through vertex at 0 index, then a unit rotation
[4, 3, 2, 1]

>>> d4.apply((1, 2), (1, 2)) # reflection between vertices at indices 1 and 2, applied twice. |(1, 2)| = 2
[1, 2, 3, 4]
```

and so on. Determine the composition of symmetries as follows:

```
>>> d3 = dihedral()
>>> my_sym = d3.apply(2, (0, ))
>>> d3.determine(my_sym)
(2,)
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
```

Thank you for reading this far!