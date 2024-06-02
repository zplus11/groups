
[Next - Maps](Maps.md)

[Previous - Subgroups](Subgroups.md)

### Cosets, Normal Subgroups and Factor Groups

If *H* is a subgroup of *G,* then for some *a* in *G,* the set {*ah*: *h* in *H*} is called the left coset of *H* in *G* containing *a.* Subsequently, corresponding right coset is the set {*ha*: *h* in *H*}. We can form cosets in `groups` as follows:

```python
>>> e = EDP(U(8), K4())
>>> s = e.subgroups()[3] # get any certain subgroup
>>> e.coset(s, (3, "b")) # (left) coset by element (3, "b") of subgroup s in group e
{(3, 'a'), (3, 'b')}
>>> e.coset(s, (3, "b"), "r")
{(3, 'b'), (3, 'a')} # right coset
```

Find the cosets of *H* = {1, 15} in *U*(32).

```python
>>> g = U(32)
>>> h = {1, 15}
>>> g.cosets(h)
[{3, 13}, {11, 5}, {9, 7}, {17, 31}, {19, 29}, {25, 23}, {27, 21}]
```

#### Normal Subgroups

A subgroup *H* of *G* is said to be normal in *G* if the left coset by every element is equal to the right counterpart. Check if a subgroup is normal or not:

```python
>>> g = D(8)
>>> h1 = {'r4', 's5', 's1', 'r0', 's3', 'r2'}
>>> h2 = {'s1', 'r0'}
>>> g.check_nsubgroup(h1)
True
>>> g.check_nsubgroup(h2)
False
```

Find all normal subgroups:

```python
>>> g.nsubgroups()
[G({'r0'}), G({'r0', 'r3'}), G({'r4', 'r0', 'r2'}), G({'r4', 'r3', 'r5', 'r1', 'r0', 'r2'}), G({'r4', 's4', 's0', 'r2', 'r0', 's2'}), G({'r4', 's5', 's1', 'r0', 's3', 'r2'}), G({'r4', 'r3', 's4', 's5', 'r5', 's1', 's0', 'r1', 'r0', 's2', 's3', 'r2'})]
>>> # show in a better form
>>> for i in _:
...     i
...
G({'r0'})
G({'r0', 'r3'})
G({'r4', 'r0', 'r2'})
G({'r4', 'r3', 'r5', 'r1', 'r0', 'r2'})
G({'r4', 's4', 's0', 'r2', 'r0', 's2'})
G({'r4', 's5', 's1', 'r0', 's3', 'r2'})
G({'r4', 'r3', 's4', 's5', 'r5', 's1', 's0', 'r1', 'r0', 's2', 's3', 'r2'})
```

#### Factor Groups

Let *G* be a group and *H* a normal subgroup of it. Then, the set *G/H* = {*aH*: *a* in *G*} forms a group under the operation (*aH*)(*bH*) = *abH,* and is called the Factor Group of G by H. Elements of a Factor Group in `groups` are denoted by group members that form the respective ``coset class.''

Form a factor group using `factor_group()` method, as shown below:

```python
>>> g = Z(18)
>>> h = g.generate(6)
>>> gBh = g.factor_group(h)
>>> gBh
G({0, 1, 2, 3, 4, 5})
```

Factor group of *D*(4) by *K* = {*R*<sub>0</sub>, *R*<sub>180</sub>}:

```python
>>> k = {"r0", "r2"}
>>> D(4).factor_group(k)
G({'r1', 'r0', 's0', 's1'})
>>> _.cayley()
0 = r0
1 = r1
2 = s0
3 = s1
------------------
     0   1   2   3

0    0 | 1 | 2 | 3
1    1 | 0 | 3 | 2
2    2 | 3 | 0 | 1
3    3 | 2 | 1 | 0
```

<br>

[Next - Maps](Maps.md)

[Previous - Subgroups](Subgroups.md)