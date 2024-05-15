# groups\definitions\edp.py

from groups.core import group
from itertools import product


class edp(group):
    """EDP of a finite number of groups"""

    # EDP (External Direct Product) of n groups G_1, G_2, ...,
    # G_n is the group {(a_1, a_2, ..., a_n): a_i \in G_i}
    # formed under component-wise operation of each group.
    
    def __init__(self, *groups):
        """Initialised the EDP of given groups."""

        # checking each group is actually a group
        for groupobj in groups:
            assert isinstance(groupobj, group), f"Invalid group {group}"

        self.groups = groups
        self.identity = tuple([group.identity for group in self.groups])
        self.n = len(groups)
        self.members = list(product(*[group.members for group in groups]))

        super().__init__(self.identity, self.members)

    def apply(self, *operations):
        """
        Applies given operations to the identity and returns
        final image.
        """

        # confirming validity of each operation
        for operation in operations:
            assert type(operation) == tuple and len(operation) == self.n, f"Invalid operation {operation}"
            
        return tuple([
            self.groups[i].apply(*[operation[i] for operation in operations]) for i in range(self.n)
        ])

# End of edp.py
