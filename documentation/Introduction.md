# groups v1.4.0

[Next - Basic Operations](BasicOperations.md)

## Introduction

`groups` is a basic Computer Algebra System to study various finite group structures from Group Theory.

**Definition** *(Group)*. A group is a non-empty set in Mathematics, elements of which follow 4 properties namely Closure, Associativity, Existence of Identity and Existence of Inverses under a certain operation.

Study finite group structures easily with python! This library contains various modules related to select group structures in Mathematics. This is a work in continuous progress, and I hope to continue working on this and implement many more group functionalities gradually. This documentation walks you through the available modules.

A group is defined in this library with 2 characteristics: the set of its members, and the function that defines how given group members are operated on the identity.

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

[1]	The `groups\symmetries\dihedral.py` module implements the idea of polygon symmetries using permutations. See [this page](Dihedral.md) for more details.

## Library Usage

Import the library by running

```python
>>> from groups import *
```

<br>

[Next - Basic Operations](BasicOperations.md)