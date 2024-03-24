from .group import group


class u(group):
    def __init__(self, n: int = 1):
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"

        self.n = n

        super().__init__(1)
        
        self.members += list(filter(self.__iscoprime, range(n)))
        self.elements = {i: i for i in range(self.n)}

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return self.__product([operation for operation in args[::-1]]) % self.n

    def __iscoprime(self, number):
        p = self.n
        while number != 0:
            p, number = number, p % number
        if p == 1: return True
        else: return False

    def __product(self, l):
        p = 1
        for i in l: p = p*i
        return p
