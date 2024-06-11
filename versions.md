## Version Tracker

#### v0.0.\alpha (Oct, 2023)
Dedicated to Dihedral Groups, `groups` was originally named `symmetries`, and was made in the form of a "menu driven program," taking user input of the operations, and returning the calculated image of the polygon after each step. Minor changes followed and then eventually, I changed the menu-driven program into a class: `polygon`. After plenty of experience working on it:

## `groups`

#### v0.0.1 (19 Jan, 2024)
Still being `symmetries`, this was the initial release in its new form. This was different from the `polygon` class and featured the still-existing `dihedral` class, with much more solid shape than `polygon`.

- Initial distributable release

#### v0.1.0 (18 Mar, 2024)
Restructured a lot of things, shifting general methods such as `subgroups()` or `order()` to a parent class `group` and defining different groups in their specialised sub-classes. `symmetries` was changed to `groups`. This will be a spree of updates as I enjoyed greater vision with the new and better structure.

- Rework the structure, adding more modules including `edp.py`

#### v1.0.0 (24 Mar, 2024)
- Stable release after some optimisation
- Fixed some theory errors

#### v1.1.0 (30 Mar, 2024)
- Add `k4.py`, `q8.py`

**v1.1.1 (10 Apr, 2024):** Minor bug fixes

#### v1.2.0 (16 Apr, 2024)
- Add ability to check nature of subgroups of the group: cyclic/abelian

#### v1.3.0 (28 Apr, 2024)
- Add cosets and normal subgroups
- Other changes, e.g. now subgroups are in set() type rather than list()

#### v1.4.0 (31 May, 2024)
- Better organisation and commenting of the code
- Renaming modules to resemble standard notation; README.md reflects these changes
- Add `G.generate()`, `G.factor_group()` (latter may be improved in future...)
- Add `maps.py` defining types of morphisms; Work to be continued on it

#### v1.5.0 (11 Jun, 2024)
- Add `documentation` directory
- Add functionalities to `groups/symmetries/dihedral.py` making it a standalone sub-package