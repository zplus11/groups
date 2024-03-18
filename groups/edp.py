from .group import group

from itertools import product


class edp(group):
    def __init__(self, *groups):
        for groupobj in groups:
            assert isinstance(groupobj, group), f"Invalid group {group}"

        self.groups = groups
        self.identity = tuple([group.identity for group in self.groups])
        self.n = len(groups)
        super().__init__(self.identity)
        
        self.members = list(product(*[group.members for group in groups]))
        self.elements = {member: self.apply(member) for member in self.members}

    def apply(self, *operations):
        for operation in operations:
            assert type(operation) == tuple and len(operation) == self.n, f"Invalid operation {operation}"
        return tuple([
            self.groups[i].apply(*[operation[i] for operation in operations]) for i in range(self.n)
        ])
