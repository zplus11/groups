print("Calculate function compositions in dihedral groups easily and quickly!\nRun shelp() for a brief description of all functions.")

nos, nature = 4, "o"
if nos%2 == 0: nature = "e"

def generate_los(sides):
    los = []
    nature = "e"
    if sides % 2 == 1: nature = "o"
    if nature == "e":
        for i in range(sides):
            los.append(f"r{i}") # rotation of i*360/n degrees
        for i in range(int(sides/2)):
            los.append(f"d{i + 1}") # reflection about vertex number i + 1
        for i in range(int(sides/2)):
            los.append(f"f{i + 1}{i + 2}") # reflection about axis between vertices numbered i + 1 & i + 2
    else:
        for i in range(sides):
            los.append(f"r{i}") # rotation of i*360/n degrees
        for i in range(sides):
            los.append(f"d{i + 1}") # rotation about vertex number i + 1
    return los

def los(sides):
    nature = "o"
    if sides % 2 == 0: nature = "e"
    if nature == "e":
        for i in range(sides):
            print("r{0}: Anti clockwise rotation of {1} degrees".format(i, i*360/sides))
        for i in range(int(sides/2)):
            print("d{0}: Reflection about vertex number {0}".format(i + 1))
        for i in range(int(sides/2)):
            print("f{0}{1}: Reflection about axis between vertices numbered {0} & {1}".format(i + 1, i + 2))
    else:
        for i in range(sides):
            print("r{0}: Anti clockwise rotation of {1} degrees".format(i, i*360/sides))
        for i in range(sides):
            print("d{0}: Reflection about vertex number {0}".format(i + 1))
            
def symmetry(lok, sides = nos):
    los = generate_los(sides)
    nature = "e"
    if sides % 2 == 1: nature = "o"
    polygon = [i + 1 for i in range(sides)]
    original = polygon.copy()
    keys = [element.strip() for element in lok.split(",")]
    keys.reverse()
    print(f"Processing the symmetries in order: {keys}")
    print(sides)
    print(los)
    if all(key in los for key in keys):
        for key in keys:
            index = int(key[-1])
            if key.startswith("r"):
                for j in range(sides):
                    new_vertex = (polygon[j] + index) % sides
                    if new_vertex == 0:
                        new_vertex = sides
                    polygon[j] = new_vertex
            elif key.startswith("f"):
                for j in range(int(sides/2)):
                    temp_vertex = polygon[index + j - 1]
                    polygon[(index + j - 1) % sides] = polygon[index - j - 2]
                    polygon[(index - j - 2) % sides] = temp_vertex
            elif key.startswith("d"):
                if nature == "e":
                    for j in range(int(sides/2) - 1):
                        temp_vertex = polygon[(index + j) % 2]
                        polygon[(index + j) % sides] = polygon[index - j - 2]
                        polygon[index - j - 2] = temp_vertex
                else:
                    for j in range(int((sides + 1)/2) - 1):
                        temp_vertex = polygon[(index + j) % sides]
                        polygon[(index + j) % sides] = polygon[index - j - 2]
                        polygon[index - j - 2] = temp_vertex
                
        print(f"Success. Final image:\nOriginal:\t{original}\nUpdated:\t{polygon}")
    else:
        print("At least one of them was not a valid symmetry. Try again. See below the list of valid symmetry for your polygon:")
        print(f"Polygon:\t{polygon}\nSymmetries:\t{los}")

def shelp():
    print("Dihedral Group Symmetries. The following functions are available:\n--- shelp(): This.\n--- symmetry('string', n): where 'string' is the list of symmetries you want to apply (separate them with comma) and 'n' is the number of sides in your polygon.\n--- los(n): Generate the list of valid symmetries for a regular polygon of sides 'n'\n--- ssource(): To get the link of github repo.")

def ssource():
    print("https://github.com/zplus11/symmetries.git")
