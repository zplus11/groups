# groups\core\group.py

from itertools import combinations
from functools import lru_cache
import string


class G:
    """Parent class for defining a group structure."""
    
    def __init__(self, members: set, function, check: bool = True):

        self.members = members
        assert callable(function)
        self.apply = function
        self.identity = None
        for member in self.members:
            if all(self.apply(member, x) == x == self.apply(x, member) for x in self.members):
                self.identity = member
        assert self.identity is not None, f"No identity found in the group."
        # Checking group properties.
        if check: assert self.__is_group()

    def __str__(self):
        """Prints the group."""

        return str(self.members)

    def __repr__(self):
        """Represents the group."""

        return f"G({repr(self.members)})"

    def __len__(self):
        """Length of the group."""

        return len(self.members)

    def __iter__(self):
        """Iterates through group members."""
        
        for x in sorted(self.members):
            yield x

    # Group properties
    def check_closure(self, members):
        """Checks for closure among members."""

        if any(self.apply(x, y) not in members for x in members for y in members):
            return False
        return True

    def check_associativity(self, members):
        """Checks for associativity among members."""
        
        if any(self.apply(self.apply(x, y), z) != self.apply(x, self.apply(y, z)) \
               for x in members for y in members for z in members):
            return False
        return True

    def check_identity(self, members):
        """Checks property of identity."""
        
        if any(not self.apply(x, self.identity) == x == self.apply(self.identity, x) for x in members):
            return False
        return True

    def check_inverses(self, members):
        """Checks for existence of inverses."""

        if any(not self.apply(self.inverse(x), x) == self.identity == self.apply(x, self.inverse(x)) for x in members):
            return False
        return True

    def __is_group(self):
        """Checks all group properties."""

        return self.check_closure(self) \
               and self.check_associativity(self) \
               and self.check_identity(self) \
               and self.check_inverses(self)
    
    def abelian(self, sub = None):
        """Checks whether the group is abelian or not."""
        
        members = self
        # if a particular subgroup is to be checked
        if sub is not None:
            if isinstance(sub, G): members = sub.members
            else:
                assert type(sub) in [list, tuple, set], f"Invalid type {type(sub)} of {sub}"
                members = sub
                for member in members:
                    assert member in self, f"Invalid subgroup element {member}"
        # checking commutativity for the required members
        if any(self.apply(a, b) != self.apply(b, a) for a in members for b in members):
            return False
        return True

    def cyclic(self, sub = None):
        """Checks whether the group is cyclic or not."""
        
        members = self
        # if a particular subgroup is to be checked
        if sub is not None:
            if isinstance(sub, G): members = sub.members
            else:
                assert type(sub) in [list, tuple, set], f"Invalid type {type(sub)} of {sub}"
                members = sub
                for member in members:
                    assert member in self, f"Invalid subgroup element {member}"
        # checking if |a| == |G| for any a in G
        for a in members:
            if self.order(a) == len(members):
                return (True, a)
        return False

    def cayley(self):
        """Prints the Cayley's Table of the group."""

        printable = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        if len(self) > 94:
            print("(!) Too many members in the group; Facing lack of printable characters.")
            printable += "◻"*(len(self)-94)
        conversion = {x: printable[i] for i, x in enumerate(self)}
        for i in conversion:
            print(conversion[i], "=", i)
        header = "     " + "   ".join(list(str(i) for i in conversion.values()))
        print("-"*len(header))
        print(header, end = "\n\n")
        for i in self:
            print(str(conversion[i]), end = "    ")
            print(" | ".join(list(str(conversion[self.apply(i, j)]) for j in self)))

    # Subgroups space
    def __generate_sublists(self, o = None):
        """Returns the potential subgroups of the group."""

        # We collect the powerset of self and filter it
        # on the basis that any subgroup H such that |H| does
        # not divide |G|, will not be a subgroup (by Lagrange's
        # Theorem).
        sublists = list(filter(
            lambda sublist: len(self) % len(sublist) == 0,
            [c for r in range(1, len(self) + 1) for c in combinations(self, r)
             if (o is None or len(c) == o)]
        ))
        return sublists
    
    @lru_cache(maxsize = None)
    def subgroups(self, order = None):
        """Returns all subgroups of given order for the group."""
        
        assert order is None or type(order) == int, f"Invalid order {order}"
        is_cyclic = self.cyclic()
        # If the group is cyclic, we apply Fundamental Theorem of
        # Cyclic Groups which states that a finite cyclic groups <a>
        # has one exactly subgroup for each other of |a|, namely
        # <a^(|a|/k)> and that is all.
        if is_cyclic and is_cyclic[0]:
            return [self.generate(self.power(is_cyclic[1], k)) \
                    for k in self.__divisors(len(self))]
        else:
            sublists = self.__generate_sublists(o = order)
            return list(G(set(a), self.apply) \
                        for a in filter(lambda sublist: self.check_subgroup(sublist), sublists))
    
    def check_subgroup(self, subset: set):
        """Checks whether a set is a subgroup of the group."""

        # We check for a subgroup using the Finite Subgroup Test,
        # i.e., we check for closure among the subset. First, checking
        # for existence of identity.
        if self.identity not in subset:
            return False
        # confirming all elements are actual group members
        if any(i not in self for i in subset):
            return False
        # finally checking for closure
        if any(self.apply(i, j) not in subset for i in subset for j in subset):
            return False
        return True

    # Cosets
    def coset(self, subgroup, element, orientation: str = "l"):
        """
        Returns left (or right) coset of a subset by an element
        in a group.
        """
        
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"
        if not isinstance(subgroup, G): subgroup = G(subgroup, self.apply)
        assert element in self, f"Invalid member {element}"

        # By default, left coset is returned. But orientation can be
        # set to "r" in arguments to receive right coset.
        assert orientation in ["l", "r"], f"Unrecognised orientation {orientation}"
        if orientation == "l":
            return set(self.apply(element, x) for x in subgroup.members)
        else:
            return set(self.apply(x, element) for x in subgroup.members)

    def cosets(self, subgroup):
        """Returns all distinct cosets of a subgroup in the group."""

        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"
        if not isinstance(subgroup, G): subgroup = G(subgroup, self.apply)
        cosets = []
        H = subgroup.members.copy()
        rest = {x for x in self if x not in H}
        while rest:
            nc = self.coset(subgroup, list(rest)[0])
            cosets.append(nc)
            H = H.union(nc)
            rest = {x for x in self if x not in H}
        return cosets
            
    # Normal subgroups
    def check_nsubgroup(self, subgroup):
        """Checks whether a subgroup is normal in the group."""
        
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"
        if not isinstance(subgroup, G): subgroup = G(subgroup, self.apply)
        # Theorem. A subgroup H of G is normal in G if aH == Ha
        # for all a in G, i.e., if left and right cosets of H by a
        # are equal for each a in G.
        for x in self:
            if self.coset(subgroup, x, "l") != self.coset(subgroup, x, "r"):
                return False
        return True

    def nsubgroups(self, order = None):
        """Returns all subgroups that are normal in the group."""

        # We simply find all subgroups then filter them using
        # self.check_nsubgroup method.
        subgroups = self.subgroups(order)
        return list(filter(lambda sub: self.check_nsubgroup(sub.members), subgroups))

    def factor_group(self, nsubgroup):
        """
        Returns the Factor Group G/H = {aH: a in G} under
        (aH)(bH) = abH.
        """

        assert self.check_nsubgroup(nsubgroup), f"Invalid normal subgroup {nsubgroup}"
        # We first collect the distinct left cosets of H in G.
        members = [self.identity]
        for x in self:
            # aH = bH <=> a^(-1)b in H.
            if not any(self.apply(x, self.inverse(y)) in nsubgroup for y in members):
                members.append(x)
        # Now we partition the group elements by matter of coset
        # distinction. We form a mapping.
        mapping = {}
        for x in self:
            tcst = self.coset(nsubgroup, x)
            for y in members:
                if self.coset(nsubgroup, y) == tcst:
                    mapping[x] = y
        # Finally, the group operation will map each element to
        # its "coset partition."
        def func(*els):
            return mapping[self.apply(*els)]
        return G(set(members), func, False)

    # Elements
    def power(self, element, n: int = 1):
        """Raises element to the given power."""

        return self.apply(*[element for i in range(n)])

    def generate(self, element):
        """Returns subgroup generated by a."""

        n = self.order(element)
        return G({self.power(element, i) for i in range(n)}, self.apply, False)
    
    def order(self, element = None):
        """Returns order of the group or its a member."""

        if element is None:
            return len(self)
        else:
            assert element in self, f"Invalid element {element}"
            order = None
            for i in self.__divisors(len(self)):
                if self.power(element, i) == self.identity:
                    order = i
                    break
            return order

    def inverse(self, element):
        """Returns inverse of a member under the group operation."""
        
        assert element in self, f"Invalid element {element}"
        inverse = None
        for opponent in self:
            if self.apply(element, opponent) == self.identity:
                inverse = opponent
                break
        return inverse

    def __divisors(self, n):
        """Divisors of n."""

        return filter(lambda x: n % x == 0, range(1, n + 1))

# End of group.py
