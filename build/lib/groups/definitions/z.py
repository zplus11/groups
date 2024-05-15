# groups\definitions\z.py

from groups.core import group


class z(group):
    """Modulo Addition group."""
    
    def __init__(self, n: int = 1):
        """Initialises the additive group of integers modulo n."""
        
        assert type(n) == int, "n need be numeric"
        assert n >= 1, "n need be >= 1"

        self.n = n
        self.members += list(range(n))
        
        super().__init__(0)

    def apply(self, *args):
        """
        Applies given operations to the identity and returns
        final image
        """
        
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        return sum([operation for operation in args[::-1]]) % self.n

# End of z.py
