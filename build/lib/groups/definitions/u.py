# groups\definitions\u.py

from groups.core import group


class u(group):
    """Modulo Multiplication group."""
    
    def __init__(self, n: int = 1):
        """Initialises the multiplicative group of integers modulo n."""
        
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"

        self.n = n
        self.members += list(filter(self.__iscoprime, range(n)))

        super().__init__(1, self.members)

    def apply(self, *args):
        """
        Applies given operations to the identity and returns
        final image
        """
        
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return self.__product([operation for operation in args[::-1]]) % self.n

    def __iscoprime(self, number):
        """Checks whether a number is co-prime with self.n."""
        
        p = self.n
        while number != 0:
            p, number = number, p % number
        if p == 1: return True
        else: return False

    def __product(self, l):
        """Returns product of the numbers in given list."""
        
        p = 1
        for i in l: p = p*i
        return p

# End of u.py
