# groups/__init__.py

"""
groups is a basic Computer Algebra System focused on finite groups
from Group Theory. It facilitates studying group operations, orders and
inverses, normal/subgroups, and more. It is a work in progress and I hope
to further it as much as I can.
"""

from groups.version import __version__


from groups.core import group
from groups.definitions import dihedral, z, u, k4, q8, edp


__all__ = [
    "__version__",
    "group",
    "dihedral", "z", "u", "k4", "q8",
    "edp"
]

__all__.extend(
    ["core", "definitions"]
)
