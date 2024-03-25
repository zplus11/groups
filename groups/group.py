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
    def subgroups(self, order: int = None):
        assert order is None or type(order) == int, f"Invalid order {order}"
        first_slice = filter(lambda sublist: 1 <= len(sublist) <= int(len(self.members)/2), self.__generate_sublists())
        if order is None:
            sublists_to_check = filter(lambda sublist: len(self.members) % len(sublist) == 0, first_slice)
        else:
            sublists_to_check = filter(lambda sublist: len(sublist) == order, first_slice)
        return list(filter(lambda sublist: self.check_subgroup(sublist), sublists_to_check))
    
    def check_subgroup(self, subset: list):
        if self.identity not in subset:
            return False
        elif any(i not in self.members for i in subset):
            return False
        elif any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        else:
            return True

    def __generate_sublists(self):
        sublists = [list(c) for r in range(len(self.members) + 1) for c in combinations(self.members, r)]
        return sublists
