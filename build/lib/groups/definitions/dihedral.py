# groups\definitions\dihedral.py

from groups.core import group


class dihedral(group):
    """Group of symmetries of a regular polygon."""
    
    def __init__(self, sides: int = 3):
        """Initialises dihedral group for an n-sided polygon."""
        
        assert type(sides) == int, "sides need be numeric"
        assert sides >= 3, "sides need be >= 3"

        self.sides = sides
        self.__state = [i + 1 for i in range(self.sides)]
        self.nature = self.sides % 2 == 0

        # Populating the group members. This is done conditionally
        # depending upon the number of sides n. First of all, we add
        # rotations (n multiples of the unit rotation). For reflections,
        # we treat as follows: If n is odd, they will be about each
        # vertex and that is it. However, if n is even, the reflections
        # are of two types, namely those passing through first half
        # of the vertices, and those passing between first half+1
        # vertices taken two at a time.
        self.members = [i for i in range(self.sides)]
        if self.nature:
            self.members += [(i,) for i in range(int(self.sides/2))]
            self.members += [(i, i + 1) for i in range(int(self.sides/2))]
        else:
            self.members += [(i,) for i in range(self.sides)]

        super().__init__(0, self.members)
        
    def apply(self, *operations):
        """
        Applies given operations to the identity and returns
        final image.
        """

        # confirming each operation is a group member
        for operation in operations:
            assert operation in self.members, f"Invalid operation: {operation}"

        # initialising the state and applying operations in reverse
        # chronological order
        self.__state = [k+1 for k in range(self.sides)]
        for operation in operations[::-1]:
            # if the operation is a rotation
            if type(operation) == int:
                self.__state = self.__rotate(operation)
            # if it is a reflection
            else:
                # if reflection is about vertex
                if len(operation) == 1:
                    self.__state = self.__reflect_from_v(operation)
                # if reflection is between two vertices
                else:
                    self.__state = self.__reflect_from_m_to_m(operation)
        return self.__state

    # Rotation algorithm
    def __rotate(self, degree: int = 0):
        """Applies the unit rotation given number of times."""

        # We make a copy of the current image and change this copy
        # accordingly. To n rotations, the vertices at k index will be
        # replaced by vertex at k - n index. Slicing takes care of it
        # easier than expected.
        temp = self.__temp()
        for index in range(len(temp)):
            temp[index] = self.__state[(index - degree)]
        self.__state = temp
        return self.__state

    # Reflecting about a vertex
    def __reflect_from_v(self, vertex: tuple = (0, )):
        """Applies the reflection about given vertex."""

        # It works.
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(1, int((self.sides + (self.sides % 2))/2)):
            temp[(base + suffix) % self.sides] = self.__state[(base - suffix)]
            temp[(base - suffix)] = self.__state[(base + suffix) % self.sides]
        self.__state = temp
        return self.__state

    # Reflecting between two vertices
    def __reflect_from_m_to_m(self, vertex: tuple = (0, 1)):
        """Applies the reflection between two given vertices."""

        # It works too.
        temp = self.__temp()
        base = vertex[0]
        for suffix in range(int(self.sides/2)):
            temp[(base + suffix + 1) % self.sides] = self.__state[(base - suffix)]
            temp[(base - suffix)] = self.__state[(base + suffix + 1) % self.sides]
        self.__state = temp
        return self.__state
        
    def __temp(self):
        """Returns the copy of current state of the polygon."""
        
        return self.__state.copy()

# End of dihedral.py
