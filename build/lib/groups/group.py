from itertools import combinations
from functools import lru_cache

class group:
    def __init__(self, identity: None):
        self.members = []
        self.elements = []
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
            image = self.elements[element]
            for _ in range(i - 1): image = self.apply(self.determine(image), element)
            if image == self.identity:
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
    def subgroups(self, order: int = None):
        assert order is None or type(order) == int, f"Invalid order {order}"
        sublists = self.__generate_sublists()
        if order is not None:
            sublists = filter(lambda sublist: len(sublist) == order, sublists)
        return list(filter(lambda sublist: self.check_subgroup(sublist), sublists))
    
    def check_subgroup(self, subset: list):
        if self.identity not in subset:
            return False
        if any(i not in self.members for i in subset):
            return False
        if any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        return True

    def __generate_sublists(self):
        sublists = list(filter(
            lambda sublist: len(self.members) % len(sublist) == 0,
            [list(c) for r in range(1, len(self.members) + 1) for c in combinations(self.members, r)]
        ))
        return sublists

    def abelian(self):
        if any(self.apply(a, b) != self.apply(b, a) for a in self.members for b in self.members):
            return False
        return True

    def cyclic(self, echo = False):
        gorder = len(self.members)
        for a in self.members:
            if self.order(a) == gorder:
                if echo == True:
                    print("Generator found:", a)
                return True
        return False
