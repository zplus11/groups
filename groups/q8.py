from .group import group


class q8(group):
    def __init__(self):
        super().__init__("1")
        
        self.members += ["1", "-1", "i", "-i", "j", "-j", "k", "-k"]
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
        self.elements = {x: self.apply(x) for x in self.members}

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        result = "1"
        for x in args[::-1]:
            result = self.operations_table[result][x]
        return result
