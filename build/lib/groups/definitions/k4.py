# groups\definitions\k4.py

from groups.core import group


class k4(group):
    """Klein's 4-group."""
    
    def __init__(self):
        "Initialises K_4 group."""
        
        self.members = ["e", "a", "b", "c"]
        # Here, we define the group operations table rigorously.
        # Essentially, this is a group definition by the Cayley
        # Table.
        self.operations_table = {
            'e': {'e': 'e', 'a': 'a', 'b': 'b', 'c': 'c'},
            'a': {'e': 'a', 'a': 'e', 'b': 'c', 'c': 'b'},
            'b': {'e': 'b', 'a': 'c', 'b': 'e', 'c': 'a'},
            'c': {'e': 'c', 'a': 'b', 'b': 'a', 'c': 'e'}
        }

        super().__init__("e", self.members)

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

# End of k4.py
