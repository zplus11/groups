# groups\definitions\definition_template.py

# In groups, groups are defined in their own classes
# that derive from the group class that is parent to all.
# To define a group yourself here, you need to define the
# following aspects:
#   - its identity,
#   - its members, and
#   - how operations are defined.
# The former two are stored in the respective class
# attributes, namely self.identity and self.members. For
# the third, you need to define a method that takes group
# members as input and returns the 'image' when these
# members are operated on self.identity. Below is a basic
# structure of how the above may be done.


# Import the parent group from core
from groups import *

# Defining the mygroup class
class mygroup(group):

    def __init__(self):
        self.identity = 0
        self.members = [0, 1, 2]
        super().__init__(identity, members)

    def apply(self, *elements):
        return sum(elements) % 2


# Then, this group can be freely called and you can use
# all other methods and functionalities of other groups,
# as illustrated below:
#
# >>> mg = mygroup()
# >>> mg.members
# [0, 1, 2]
# >>> mg.apply(0, 1, 2, 2, 1)
# 0
# >>> mg.subgroups()
# [{0}, {0, 1, 2}]
# >>> mg.nsubgroups()
# [{0}, {0, 1, 2}]
# >>> mg.coset({0, 1, 2}, 2)
# {0, 1}

# End of definition_template.py
