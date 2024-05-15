# groups\core\group.py

from itertools import combinations
from functools import lru_cache
import string


class group:
    """Parent class for defining a group structure."""
    
    def __init__(self, identity: None, members: None):
        
        self.identity = identity
        self.members = members
        # Defining below a key-value pair mapping each
        # element to its image under the group operation.
        self.elements = {member: self.apply(member) for member in self.members}
        

    # Group properties
    def abelian(self, sub = None):
        """Checks whether the group is abelian or not."""
        
        members = self.members
        # if a particular subgroup is to be checked
        if sub is not None:
            assert type(sub) in [list, tuple, set], f"Invalid type {type(sub)} of {sub}"
            members = sub
            for member in members:
                assert member in self.members, f"Invalid subgroup element {member}"
        # checking commutativity for the required members
        if any(self.apply(a, b) != self.apply(b, a) for a in members for b in members):
            return False
        return True

    def cyclic(self, sub = None):
        """Checks whether the group is cyclic or not."""
        
        members = self.members
        # if a particular subgroup is to be checked
        if sub is not None:
            assert type(sub) in [list, tuple, set]
            members = sub
            for member in members:
                assert member in self.members, f"Invalid subgroup element {member}"
        # checking if |a| == |G| for any a in G
        for a in members:
            if self.order(a) == len(members):
                return True
        return False

    def cayley(self):
        """Prints the Cayley's Table of the group."""

        printable = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        if len(self.members) > 94:
            print("(!) Too many members in the group; Facing lack of printable characters.")
            printable += "◻"*(len(self.members)-94)
        conversion = {i: printable[x] for x, i in enumerate(self.members)}
        for i in conversion:
            print(conversion[i], "=", i)
        header = "     " + "   ".join(list(str(i) for i in conversion.values()))
        print("-"*len(header))
        print(header, end = "\n\n")
        for i in self.members:
            print(str(conversion[i]), end = "    ")
            print(" | ".join(list(str(conversion[self.determine(self.apply(i, j))]) for j in self.members)))

    # Subgroups space
    def __generate_sublists(self, o = None):
        """Returns the potential subgroups of the group."""

        # We collect the powerset of self.members and filter it
        # on the basis that any subgroup H such that |H| does
        # not divide |G|, will not be a subgroup (by Lagrange's
        # Theorem).
        sublists = list(filter(
            lambda sublist: len(self.members) % len(sublist) == 0,
            [c for r in range(1, len(self.members) + 1) for c in combinations(self.members, r)
             if (o is None or len(c) == o)]
        ))
        return sublists
    
    @lru_cache(maxsize = None)
    def subgroups(self, order = None):
        """Returns all subgroups of given order for the group."""
        
        assert order is None or type(order) == int, f"Invalid order {order}"
        sublists = self.__generate_sublists(o = order)
        return list(set(a) for a in filter(lambda sublist: self.check_subgroup(sublist), sublists))
    
    def check_subgroup(self, subset: set):
        """Checks whether a set is a subgroup of the group."""

        # We check for a subgroup using the Finite Subgroup Test,
        # i.e., we check for closure among the subset. First, checking
        # for existence of identity.
        if self.identity not in subset:
            return False
        # confirming all elements are actual group members
        if any(i not in self.members for i in subset):
            return False
        # finally checking for closure
        if any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        return True

    # Cosets
    def coset(self, subgroup, element, orientation: str = "l"):
        """
        Returns left (or right) coset of a subset by an element
        in a group.
        """
        
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"
        assert element in self.members, f"Invalid member {element}"

        # By default, left coset is returned. But orientation = "r"
        # can be passed in arguments to receive right coset.
        assert orientation in ["l", "r"], f"Unrecognised orientation {orientation}"
        if orientation == "l":
            return set(self.determine(self.apply(element, x)) for x in subgroup)
        else:
            return set(self.determine(self.apply(x, element)) for x in subgroup)

    # Normal subgroups
    def check_nsubgroup(self, subgroup):
        """Checks whether a subgroup is normal in the group."""
        
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"

        # Theorem. A subgroup H of G is normal in G if aH == Ha
        # for all a in G, i.e., if left and right cosets of H by a
        # are equal for each a in G.
        for x in self.members:
            if self.coset(subgroup, x, "l") != self.coset(subgroup, x, "r"):
                return False
        return True

    def nsubgroups(self, order = None):
        """Returns all subgroups that are normal in the group."""

        # We simply find all subgroups then filter them using
        # self.check_nsubgroup method.
        subgroups = self.subgroups(order)
        return list(filter(lambda sub: self.check_nsubgroup(sub), subgroups))

    # Group elements
    def determine(self, current_state):
        """
        Takes an element image and returns which member it is.
        Useful for when the images are unusually different from
        nomenchlature for computational purposes, e.g.
        groups.dihedral class.
        """
        
        assert current_state in self.elements.values(), f"Invalid image {current_state}"
        result = None
        for element in self.elements:
            if self.elements[element] == current_state:
                result = element
                break
        return result

    def order(self, element):
        """Returns order of a member of the group."""
        
        assert element in self.members, f"Invalid element {element}"
        order = None
        for i in filter(lambda x: len(self.members) % x == 0, range(1, len(self.members) + 1)):
            image = self.apply(*[element for i in range(i)])
            if image == self.elements[self.identity]:
                order = i
                break
        return order

    def inverse(self, element):
        """Returns inverse of a member under the group operation."""
        
        assert element in self.members, f"Invalid element {element}"
        inverse = None
        for opponent in self.members:
            if self.apply(element, opponent) == self.elements[self.identity]:
                inverse =  opponent
                break
        return inverse

# End of group.py
