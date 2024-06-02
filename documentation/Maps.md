
[Previous - Cosets, Normal Subgroups & Factor Groups](CosetsNormalsFactors.md)

### Maps

A map from a group *G*<sub>1</sub> to another group *G*<sub>2</sub> is a definition that takes each element of the domain group to an element of the codomain group. For example, consider the map phi from *Z*<sub>10</sub> to *Z*<sub>2</sub> given by the function f(*x*) = *x* (mod 2). We can define it as follows:

```python
>>> f = lambda x: x%2
>>> m = Map(Z(20), Z(2), f)
>>> m
𝜙: G({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}) --> G({0, 1})
>>> m(15)
1
>>> m(4)
0
```

We can check if this map is operation preserving or not as follows:

```python
>>> m.op()
True
```

#### Homomorphisms

A map phi: (*G*<sub>1</sub>, +) --> (*G*<sub>2</sub>, ~) is said to be a homomorphism if it is operation preserving, i.e, if phi(*x* + *y*) = phi(*x*)~phi(*y*) for every *x*, *y* in *G*<sub>1</sub>. We can define a homomorphism from *Z*<sub>12</sub> to itself by x --> 3x as follows:

```python
>>> phi = Homomorphism(Z(12), Z(12), lambda x: (3*x)%12)
```

Kernal of a homomorphism is the set of those elements in domain that get mapped to the identity of codomain. So,

```python
>>> phi.kernal()
{0, 8, 4}
```

Another homomorphism from *D*<sub>3</sub> to *Z*<sub>2</sub> that maps rotations to 0 and reflections to 1:

```python
>>> phi = Homomorphism(D(3), Z(2), lambda x: 0 if x.startswith("r") else 1)
>>> phi
𝜙: G({'r2', 's1', 'r1', 's2', 's0', 'r0'}) --> G({0, 1})
>>> phi.kernal()
{'r2', 'r1', 'r0'}
```

#### Other Maps

- Isomorphisms: A one-one map that is operation preserving.

```python
>>> g = G({0}, lambda *x: sum(x))
>>> f = lambda x: x
>>> Isomorphism(g, g, f)
𝜙: G({0}) --> G({0})
```

- Automorphisms: An Isomorphism from a group to itself

```python
>>> Automorphism(g, f)
𝜙: G({0}) --> G({0})
```

- Inner Automorphisms: An Automorphism induced by an element

Inner automorphisms are induced by an element. The map is defined by phi(*x*) = *axa*^(-1) for some *a* in the group. For example:

```python
>>> phi = IAutomorphism(D(4), "s3")
>>> phi("r0")
'r0'
>>> phi("s2")
's0'
```


<br>

*work to be continued on maps...*

*... and countless other things are possible if we are innovative enough!.*

<br>

[Previous - Cosets, Normal Subgroups & Factor Groups](CosetsNormalsFactors.md)