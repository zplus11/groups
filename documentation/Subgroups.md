
[Next - Cosets, Normal Subgroups & Factor Groups](CosetsNormalsFactors.md)

[Previous - Basic Operations](BasicOperations.md)

### Subgroups

If *G* is a group, then *H* its subset is said to be its subgroup if *H* forms a group itself under the operation of *G.* We can check if a subset of members is a subgroup or not using `check_subgroup()` method.

```python
>>> Z20 = Z(20)
>>> Z20.check_subgroup({2*x for x in range(10)})
True
>>> D(10).check_subgroup({"s3", "r2", "r0", "r3"})
False
>>> D(10).check_subgroup({"r0"})
True
```

Print all subgroups of a group:

```python
>>> D8_subs = D(8).subgroups()
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

This becomes expensive in Non-cyclic groups when the order is large. In cyclic groups, there is greater tolerance to large orders.

```python
>>> len(U(997).subgroups()) # Order 996 group!
12
```

List the cyclic subgroups of U<sub>30</sub> (see [this](https://math.stackexchange.com/questions/3390079/systematically-list-the-cyclic-subgroups-of-u30)):

```python
>>> U30s = U(30).subgroups()
>>> for i in u30s:
...     if U(30).cyclic(i): print(i)
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

Subgroup generated by an element of the group:

```python
>>> Z(30).generate(4)
G({0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28})
```
<br>

[Next - Cosets, Normal Subgroups & Factor Groups](CosetsNormalsFactors.md)

[Previous - Basic Operations](BasicOperations.md)