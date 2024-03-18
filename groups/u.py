from .group import group


class u(group):
    def __init__(self, n: int = 1):
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"
        assert self.__isprime(n), "n needs to be prime"

        self.n = n

        super().__init__(0)
        
        self.members += list(range(n))
        self.elements = {i: i % n for i in range(n)}

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return self.__product([operation for operation in args[::-1]]) % self.n

    def __isprime(self, number):
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                return False
        return True

    def __product(self, l):
        p = 1
        for i in l: p = p*i
        return p
