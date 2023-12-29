# symmetries

Dihedral groups: symmetries of a regular polygon. Calculate composition of functions in the group easily.

⚠️ To use the program you need to have Python installed. Download it from [here](https://www.python.org/downloads/).

⚠️ This program is still work in progress. There are bugs and glitches that need to be solved, and there is more to be done overall. It is NOWHERE near its final shape.

To still use it, clone the repository in your desired directory, then after navigating to the directory, run

```         
python
```

to start python. Then run

```         
from symmetries import *
```

to install the functions.

`symmetries` comes with a class `polygon` which can be used to define a regular polygon with `n` sides by running

```
pol = polygon(n) # replace n by integer > 2
```

and which has the following methods:
- `show()`: to print the polygon in its current shape;
- `list()`: to print a list of symmetries available for the polygon, and instructions to use:
- `apply(operations)`: to apply the operations `operations` to the polynomial.

`apply()` takes a string argument wherein you provide the operations separated by comma.

Thanks for using!