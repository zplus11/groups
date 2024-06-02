# groups/__init__.py

"""
groups is a basic Computer Algebra System focused on finite groups
from Group Theory. It facilitates studying group operations, orders and
inverses, normal/subgroups, and more. It is a work in progress and I hope
to further it as much as I can.
"""

from groups.version import __version__
from groups.group import G
from groups.definitions import D, Z, U, K4, Q8, EDP
from groups.maps import Map, Homomorphism, Isomorphism, Automorphism, IAutomorphism
from groups.symmetries import dihedral

__all__ = [
    "__version__",
    
    "G",
    "D", "Z", "U", "K4", "Q8",
    "EDP",
    "Map", "Homomorphism", "Isomorphism", "Automorphism", "IAutomorphism",
    
    "dihedral"
]

__all__.extend(["symmetries"])
