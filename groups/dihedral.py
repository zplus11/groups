from .group import group


class dihedral(group):
    def __init__(self, sides: int = 3):
        assert type(sides) == int, "sides need be numeric"
        assert sides >= 3, "sides need be >= 3"

        self.sides = sides
        self.__state = [i + 1 for i in range(self.sides)]
        self.nature = self.sides % 2 == 0

        super().__init__(0)

        self.members = [i for i in range(self.sides)]
        if self.nature:
            self.members += [(i,) for i in range(int(self.sides/2))]
            self.members += [(i, i + 1) for i in range(int(self.sides/2))]
        else:
            self.members += [(i,) for i in range(self.sides)]

        self.elements = {symmetry: self.apply(symmetry) for symmetry in self.members}
        
    def apply(self, *operations):
        for operation in operations:
            assert operation in self.members, f"Invalid operation: {operation}"

        self.__state = [k+1 for k in range(self.sides)]
        for operation in operations[::-1]:
            if type(operation) == int:
                self.__state = self.__rotate(operation)
            else:
                if len(operation) == 1:
                    self.__state = self.__reflect_from_v(operation)
                else:
                    self.__state = self.__reflect_from_m_to_m(operation)
        return self.__state

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