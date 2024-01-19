"""Python package to study Dihedral group structures using permutations"""
 
from itertools import combinations


class dihedral:
    """class to define dihedral group with n sides"""
    def __init__(self, sides: int = 3):
        assert sides >= 3, "Sides need be >= 3"

        self.sides = sides
        self.state = [i + 1 for i in range(self.sides)]
        self.rotations = [i for i in range(self.sides)]
        self.nature = self.sides % 2 == 0

        self.reflections = []
        if self.nature:
            self.reflections += [(i,) for i in range(int(self.sides/2))]
            self.reflections += [(i, i + 1) for i in range(int(self.sides/2))]
        else:
            self.reflections += [(i,) for i in range(self.sides)]

        self.symmetries = self.rotations + self.reflections
        self.elements = {symmetry: self.apply(symmetry) for symmetry in self.symmetries}
        
    def apply(self, *args):
        for operation in args:
            assert operation in self.symmetries, f"Invalid operation: {operation}"

        self.state = self.__init_pol()
        for operation in args:
            if type(operation) == int:
                self.state = self.__rotate(operation)
            else:
                if len(operation) == 1:
                    self.state = self.__reflect_from_v(operation)
                else:
                    self.state = self.__reflect_from_m_to_m(operation)
        reserve = self.state
        self.state = self.__init_pol()
        return reserve

    def determine(self, current_state):
        result = None
        for symmetry in self.elements:
            if self.elements[symmetry] == current_state:
                result = symmetry
                break
        return result

    def subgroups(self):
        subgroups = [[0]]
        sublists_to_check = [sublist for sublist in self.__generate_sublists() if 2 <= len(sublist) <= int(len(self.symmetries)/2)]
        for sublist in sublists_to_check:
            if len(self.symmetries) % len(sublist) == 0:
                if self.check_subgroup(sublist):
                    subgroups.append(sublist)
        subgroups.append(self.symmetries)
        return subgroups

    def check_subgroup(self, subset: list):
        if 0 not in subset:
            return False
        elif any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        else:
            return True

    def __rotate(self, degree: int = 0):
        temp = self.__temp()
        for index in range(len(temp)):
            temp[index] = self.state[(index - degree)]
        self.state = temp
        return self.state

    def __reflect_from_v(self, vertex: tuple = (0, )):
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(1, int((self.sides + (self.sides % 2))/2)):
            temp[(base + suffix) % self.sides] = self.state[(base - suffix)]
            temp[(base - suffix)] = self.state[(base + suffix) % self.sides]
        self.state = temp
        return self.state

    def __reflect_from_m_to_m(self, vertex: tuple = (0, 1)):
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(int(self.sides/2)):
            temp[(base + suffix + 1) % self.sides] = self.state[(base - suffix)]
            temp[(base - suffix)] = self.state[(base + suffix + 1) % self.sides]
        self.state = temp
        return self.state
        
    def __temp(self):
        return self.state.copy()

    def __init_pol(self):
        return [k + 1 for k in range(self.sides)]

    def __generate_sublists(self):
        sublists = [list(c) for r in range(len(self.symmetries) + 1) for c in combinations(self.symmetries, r)]
        return sublists
