# groups\definitions\q8.py

from groups.core import group


class q8(group):
    """"Quaternion group."""
    
    def __init__(self):
        """Initialises Q_8 group."""
        
        self.members += ["1", "-1", "i", "-i", "j", "-j", "k", "-k"]
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
        
        super().__init__("1", self.members)
        

    def apply(self, *args):
        """
        Applies given operations to the identity and returns
        final image
        """
        
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        result = "1"
        for x in args[::-1]:
            result = self.operations_table[result][x]
        return result

# End of q8.py
