from groups.group import G
from itertools import product


class D(G):
    """Dihedral group of order 2n."""

    def __init__(self, n: int = 3):
        assert type(n) == int, "n need be numeric"
        assert n >= 3, "n need be >= 3"

        self.members = {f"r{i}" for i in range(n)}.union({f"s{i}" for i in range(n)})
        identity = "r0"
        self.n = n
        
        super().__init__(self.members, self.apply, False)

    def apply(self, *symmetries):
        for sym in symmetries:
            assert sym in self.members, f"Invalid member {sym}"
        e = "r0"
        for sym in symmetries:
            if e[0] == "r":
                if sym[0] == "r":
                    e = "r" + str((int(e[1:]) + int(sym[1:])) % self.n)
                else:
                    e = "s" + str((int(e[1:]) + int(sym[1:])) % self.n)
            else:
                if sym[0] == "r":
                    e = "s" + str((int(e[1:]) - int(sym[1:])) % self.n)
                else:
                    e = "r" + str((int(e[1:]) - int(sym[1:])) % self.n)
        return e

class EDP(G):
    """EDP of a finite number of groups"""

    def __init__(self, *groups):
        # EDP (External Direct Product) of n groups G_1, G_2, ...,
        # G_n is the group {(a_1, a_2, ..., a_n): a_i \in G_i}
        # formed under component-wise operation of each group.

        # checking each group is actually a group
        for groupobj in groups:
            assert isinstance(groupobj, G), f"Invalid group {groupobj}"
        self.groups = groups
        self.n = len(groups)
        identity = tuple([group.identity for group in groups])
        self.members = set(product(*[group.members for group in groups]))

        super().__init__(self.members, self.apply, False)
        
    def apply(self, *operations):
        # confirming validity of each operation
        for operation in operations:
            assert operation in self.members, f"Invalid operation {operation}"
            
        return tuple([
            self.groups[i].apply(*[operation[i] for operation in operations]) for i in range(self.n)
        ])

class K4(G):
    """Klein's 4-group."""

    def __init__(self):
        self.members = {"e", "a", "b", "c"}
        # Here, we define the group operations table rigorously.
        # Essentially, this is a group definition by the Cayley
        # Table.
        self.operations_table = {
            'e': {'e': 'e', 'a': 'a', 'b': 'b', 'c': 'c'},
            'a': {'e': 'a', 'a': 'e', 'b': 'c', 'c': 'b'},
            'b': {'e': 'b', 'a': 'c', 'b': 'e', 'c': 'a'},
            'c': {'e': 'c', 'a': 'b', 'b': 'a', 'c': 'e'}
        }
        super().__init__(self.members, self.apply, False)

    def apply(self, *args):
        """
        Applies given operations to the identity and returns
        final image.
        """
        
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        result = "e"
        for x in args[::-1]:
            result = self.operations_table[result][x]
        return result

class Q8(G):
    """Klein's 4-group."""

    def __init__(self):
        self.members = {"1", "-1", "i", "-i", "j", "-j", "k", "-k"}
        # Here, we define the group operations table rigorously.
        # Essentially, this is a group definition by the Cayley
        # Table.
        self.operations_table = {
            '1': {'1': '1', '-1': '-1', 'i': 'i', '-i': '-i', 'j': 'j', '-j': '-j', 'k': 'k', '-k': '-k'},
            '-1': {'1': '-1', '-1': '1', 'i': '-i', '-i': 'i', 'j': '-j', '-j': 'j', 'k': '-k', '-k': 'k'},
            'i': {'1': 'i', '-1': '-i', 'i': '-1', '-i': '1', 'j': 'k', '-j': '-k', 'k': '-j', '-k': 'j'},
            '-i': {'1': '-i', '-1': 'i', 'i': '1', '-i': '-1', 'j': '-k', '-j': 'k', 'k': 'j', '-k': '-j'},
            'j': {'1': 'j', '-1': '-j', 'i': '-k', '-i': 'k', 'j': '-1', '-j': '1', 'k': 'i', '-k': '-i'},
            '-j': {'1': '-j', '-1': 'j', 'i': 'k', '-i': '-k', 'j': '1', '-j': '-1', 'k': '-i', '-k': 'i'},
            'k': {'1': 'k', '-1': '-k', 'i': 'j', '-i': '-j', 'j': '-i', '-j': 'i', 'k': '-1', '-k': '1'},
            '-k': {'1': '-k', '-1': 'k', 'i': '-j', '-i': 'j', 'j': 'i', '-j': '-i', 'k': '1', '-k': '-1'},
        }
        super().__init__(self.members, self.apply, False)

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        result = "1"
        for x in args[::-1]:
            result = self.operations_table[result][x]
        return result


class U(G):
    """Initialises the multiplicative group of integers modulo n."""

    def __init__(self, n: int = 1):
        self.n = n
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"
            
        self.members = set(filter(self.__iscoprime, range(self.n)))
        if n == 1: self.members = {1}

        super().__init__(self.members, self.apply, False)

    def __iscoprime(self, number):
        p = self.n
        while number != 0:
            p, number = number, p % number
        if p == 1: return True
        else: return False
            
    def product(self, l):
        p = 1
        for i in l: p = p*i
        return p

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return self.product([operation for operation in args[::-1]]) % self.n


class Z(G):
    """Initialises the additive group of integers modulo n."""
    
    def __init__(self, n: int = 1):
        self.n = n
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"
            
        self.members = set(range(self.n))
        super().__init__(self.members, self.apply, False)

    def apply(self, *args):
        """
        Applies given operations to the identity and returns
        final image.
        """
        
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return sum([operation for operation in args[::-1]]) % self.n
