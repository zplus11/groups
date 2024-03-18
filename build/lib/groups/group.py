from itertools import combinations

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

    def subgroups(self):
        subgroups = []
        sublists_to_check = [sublist for sublist in self.__generate_sublists() if 1 <= len(sublist) <= int(len(self.members)/2)]
        for sublist in sublists_to_check:
            if len(self.members) % len(sublist) == 0:
                if self.check_subgroup(sublist):
                    subgroups.append(sublist)
        subgroups.append(self.members)
        return subgroups
    
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
