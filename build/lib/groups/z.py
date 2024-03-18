from .group import group


class z(group):
    def __init__(self, n: int = 1):
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"

        self.n = n

        super().__init__(0)
        
        self.members += list(range(n))
        self.elements = {i: i % n for i in range(n)}

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return sum([operation for operation in args[::-1]]) % self.n
