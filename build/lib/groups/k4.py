from .group import group


class k4(group):
    def __init__(self):
        super().__init__("e")
        
        self.members += ["e", "a", "b", "c"]
        self.operations_table = {
            'e': {'e': 'e', 'a': 'a', 'b': 'b', 'c': 'c'},
            'a': {'e': 'a', 'a': 'e', 'b': 'c', 'c': 'b'},
            'b': {'e': 'b', 'a': 'c', 'b': 'e', 'c': 'a'},
            'c': {'e': 'c', 'a': 'b', 'b': 'a', 'c': 'e'}
        }
        self.elements = {x: self.apply(x) for x in self.members}

    def apply(self, *args):
        for operation in args:
            assert operation in self.members, f"Invalid operation: {operation}"

        result = "e"
        for x in args[::-1]:
            result = self.operations_table[result][x]
        return result
