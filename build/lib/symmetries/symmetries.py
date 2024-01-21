"""Python package to study Dihedral group structures using permutations"""
 
from itertools import combinations


class dihedral:
    """class to define dihedral group with n sides"""
    def __init__(self, sides: int = 3):
        """define dihedral group"""
        
        assert sides >= 3, "Sides need be >= 3"

        self.sides = sides
        self.__state = [i + 1 for i in range(self.sides)]
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
        """apply one or more symmetries listed in self.symmetries"""

        for operation in args:
            assert operation in self.symmetries, f"Invalid operation: {operation}"

        self.__state = self.__init_pol()
        for operation in args:
            if type(operation) == int:
                self.__state = self.__rotate(operation)
            else:
                if len(operation) == 1:
                    self.__state = self.__reflect_from_v(operation)
                else:
                    self.__state = self.__reflect_from_m_to_m(operation)
        reserve = self.__state
        self.__state = self.__init_pol()
        return reserve

    def determine(self, current_state):
        """determine the group element that a certain symmetry is"""
        
        result = None
        for symmetry in self.elements:
            if self.elements[symmetry] == current_state:
                result = symmetry
                break
        return result

    def subgroups(self):
        """get subgroups of the dihedral group"""
        
        subgroups = [[0]]
        sublists_to_check = [sublist for sublist in self.__generate_sublists() if 2 <= len(sublist) <= int(len(self.symmetries)/2)]
        for sublist in sublists_to_check:
            if len(self.symmetries) % len(sublist) == 0:
                if self.check_subgroup(sublist):
                    subgroups.append(sublist)
        subgroups.append(self.symmetries)
        return subgroups

    def check_subgroup(self, subset: list):
        """check if a certain set is a subgroup or not"""
        
        if 0 not in subset:
            return False
        elif any(self.determine(self.apply(i, j)) not in subset for i in subset for j in subset):
            return False
        else:
            return True

    def __rotate(self, degree: int = 0):
        temp = self.__temp()
        for index in range(len(temp)):
            temp[index] = self.__state[(index - degree)]
        self.__state = temp
        return self.__state

    def __reflect_from_v(self, vertex: tuple = (0, )):
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(1, int((self.sides + (self.sides % 2))/2)):
            temp[(base + suffix) % self.sides] = self.__state[(base - suffix)]
            temp[(base - suffix)] = self.__state[(base + suffix) % self.sides]
        self.__state = temp
        return self.__state

    def __reflect_from_m_to_m(self, vertex: tuple = (0, 1)):
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(int(self.sides/2)):
            temp[(base + suffix + 1) % self.sides] = self.__state[(base - suffix)]
            temp[(base - suffix)] = self.__state[(base + suffix + 1) % self.sides]
        self.__state = temp
        return self.__state
        
    def __temp(self):
        return self.__state.copy()

    def __init_pol(self):
        return [k + 1 for k in range(self.sides)]

    def __generate_sublists(self):
        sublists = [list(c) for r in range(len(self.symmetries) + 1) for c in combinations(self.symmetries, r)]
        return sublists
