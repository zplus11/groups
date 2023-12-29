"""python program to calculate Dihedral group symmetries easily"""

def f_applysymmetries(keys, polygon):
    n = len(polygon)
    ops = [key.lower().strip() for key in keys.split(",")[::-1]]
    if all(op in f_getlos(n) for op in ops):
        for key in ops:
            index = int(key[-1])
            if key.startswith("r"):
                for j in range(n):
                    new_vertex = (polygon[j] + index) % n
                    if new_vertex == 0:
                        new_vertex = n
                    polygon[j] = new_vertex
            elif key.startswith("f"):
                for j in range(int(n/2)):
                    temp_vertex = polygon[index + j - 1]
                    polygon[(index + j - 1) % n] = polygon[index - j - 2]
                    polygon[(index - j - 2) % n] = temp_vertex
            elif key.startswith("d"):
                if n % 2 == 0:
                    for j in range(int(n/2) - 1):
                        temp_vertex = polygon[(index + j) % 2]
                        polygon[(index + j) % n] = polygon[index - j - 2]
                        polygon[index - j - 2] = temp_vertex
                else:
                    for j in range(int((n + 1)/2) - 1):
                        temp_vertex = polygon[(index + j) % n]
                        polygon[(index + j) % n] = polygon[index - j - 2]
                        polygon[index - j - 2] = temp_vertex
    return polygon

def f_getlos(n):
    los = {}
    if n % 2 == 0:
        for i in range(n):
            los[f"r{i}"] = f"Anti clockwise rotation of {i*360/n} degrees" # rotation of i*360/n degrees
        for i in range(int(n/2)):
            los[f"d{i + 1}"] = f"Reflection about vertex number {i + 1}" # reflection about vertex number i + 1
        for i in range(int(n/2)):
            los[f"f{i + 1}{i + 2}"] = f"Reflection about axis between vertices numbered {i + 1} & {i + 2}" # reflection about axis between vertices numbered i + 1 & i + 2
    else:
        for i in range(n):
            los[f"r{i}"] = f"Anti clockwise rotation of {i*360/n} degrees" # rotation of i*360/n degrees
        for i in range(n):
            los[f"d{i + 1}"] = f"Reflection about vertex number {i + 1}" # rotation about vertex number i + 1
    return los


class polygon:
    def __init__(self, sides: int):
        assert sides > 2, "Number of sides must be more than 2 (two)"
        self.sides = sides
        self.polygon = {i: i + 1 for i in range(sides)}
        self.los = f_getlos(self.sides)
        
    def list(self):
        """list available symmetries for the polygon"""
        
        print(f"Printing symmetries of regular polygon with {self.sides} sides")
        for s in self.los:
            print(s + ":", self.los[s])
        print("To apply the operations, use 'apply(str)' method where str must be a string of the above symmetries separated by comma. e.g.: square.apply('r0, r3, d1')")
        
    def show(self):
        """show the polygon in its current shape"""
        
        print("The polygon in current shape is:")
        print([i for i in self.polygon.values()])

    def apply(self, operations: str = "r0"):
        """apply symmetries to the polygon. separate the operations in list() method by commas"""
        
        o_polygon = [i for i in self.polygon.copy().values()]
        self.polygon = f_applysymmetries(operations, self.polygon)
        print("Operations applied. The polygon was changed from")
        print(o_polygon)
        print("to")
        print([i for i in self.polygon.values()])


triangle = polygon(3)
square = polygon(4)
pentagon = polygon(5)
hexagon = polygon(6)
