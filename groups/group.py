from itertools import combinations
from functools import lru_cache
import string


class group:
    def __init__(self, identity: None):
        self.members = []
        self.elements = {}
        self.identity = identity

    def determine(self, current_state):
        result = None
        for element in self.elements:
            if self.elements[element] == current_state:
                result = element
                break
        return result

    def order(self, element):
        assert element in self.members, f"Invalid element {element}"
        order = None
        for i in filter(lambda x: len(self.members) % x == 0, range(1, len(self.members) + 1)):
            image = self.apply(*[element for i in range(i)])
            if image == self.elements[self.identity]:
                order = i
                break
        return order

    def inverse(self, element):
        assert element in self.members, f"Invalid element {element}"
        inverse = None
        for opponent in self.members:
            if self.apply(element, opponent) == self.elements[self.identity]:
                inverse =  opponent
                break
        return inverse

    @lru_cache(maxsize = None)
    def subgroups(self, order = None):
        assert order is None or type(order) == int, f"Invalid order {order}"
        sublists = self.__generate_sublists(o = order)
        return list(set(a) for a in filter(lambda sublist: self.check_subgroup(sublist), sublists))
    
    def check_subgroup(self, subset: set):
        if self.identity not in subset:
            return False
        if any(i not in self.members for i in subset):
            return False
        if any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        return True

    def __generate_sublists(self, o = None):
        sublists = list(filter(
            lambda sublist: len(self.members) % len(sublist) == 0,
            [c for r in range(1, len(self.members) + 1) for c in combinations(self.members, r)
             if (o is None or len(c) == o)]
        ))
        return sublists

    def coset(self, subgroup, element, orientation: str = "l"):
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"
        assert element in self.members, f"Invalid member {element}"

        assert orientation in ["l", "r"], f"Unrecognised orientation {orientation}"
        if orientation == "l":
            return set(self.determine(self.apply(element, x)) for x in subgroup)
        else:
            return set(self.determine(self.apply(x, element)) for x in subgroup)

    def check_nsubgroup(self, subgroup):
        assert self.check_subgroup(subgroup), f"Invalid subgroup {subgroup}"

        for x in self.members:
            if self.coset(subgroup, x, "l") != self.coset(subgroup, x, "r"):
                return False
        return True

    def nsubgroups(self, order = None):
        subgroups = self.subgroups(order)
        return list(filter(lambda sub: self.check_nsubgroup(sub), subgroups))

    def abelian(self, sub = None):
        members = self.members
        if sub is not None:
            assert type(sub) in [list, tuple, set]
            members = sub
            for member in members:
                assert member in self.members, f"Invalid subgroup element {member}"
        if any(self.apply(a, b) != self.apply(b, a) for a in members for b in members):
            return False
        return True

    def cyclic(self, sub = None):
        members = self.members
        if sub is not None:
            assert type(sub) in [list, tuple, set]
            members = sub
            for member in members:
                assert member in self.members, f"Invalid subgroup element {member}"
        for a in members:
            if self.order(a) == len(members):
                return True
        return False

    def cayley(self):
        printable = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        if len(self.members) > 94:
            print("(!) Too many members in the group; Fcing lack of printable characters.")
            printable += "◻"*(len(self.members)-94)
        conversion = {i: printable[x] for x, i in enumerate(self.members)}
        for i in conversion:
            print(conversion[i], "=", i)
        header = "   | " + " | ".join(list(str(i) for i in conversion.values()))
        print("-"*len(header))
        print(header, end = "\n\n")
        for i in self.members:
            print(str(conversion[i]), end = "  | ")
            print(" | ".join(list(str(conversion[self.determine(self.apply(i, j))]) for j in self.members)))
                
