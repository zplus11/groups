sides = 9
nature = "o"
if sides%2 == 0:
    nature = "e"
polygon = [i + 1 for i in range(sides)]
original = [i + 1 for i in range(sides)]
los = []
if nature == "e":
    for i in range(sides):
        #print("r{0}: anti-clockwise rotation of {1} degrees".format(i, i*360/sides))
        los.append(f"r{i}")
    for i in range(int(sides/2)):
        #print("d{0}: reflection about vertex {1}".format(i, i + 1))
        los.append(f"d{i}")
    for i in range(int(sides/2)):
        #print("f{0}: reflection about axis between vertices {1} and {2}".format(i, i + 1, i + 2))
        los.append(f"f{i}")
else:
    for i in range(sides):
        #print("r{0}: anti-clockwise rotation of {1} degrees".format(i, i*360/sides))
        los.append(f"r{i}")
    for i in range(sides):
        #print("d{0}: reflection about the vertex {1}".format(i, i + 1))
        los.append(f"d{i}")

def process_symmetry(lok):
    print(lok)
    keys = [element.strip() for element in lok.split(",")]
    if all(key in los for key in keys):
        for key in keys:
            index = int(key[-1])
            if key.startswith("r"):
                for j in range(sides):
                    new_vertex = (polygon[j] + index) % sides
                    if new_vertex == 0:
                        new_vertex = sides
                    polygon[j] = new_vertex
        print(f"Success.\nOriginal:\t{original}\nUpdated:\t{polygon}")
    else:
        print("At least one of them was not a valid symmetry. Try again. See below the list of valid symmetry for your polygon:")
        print(f"Polygon:\t{polygon}\nSymmetries:\t{los}")
        print("Feed number of sides to the 'sides' variable to change number of sides.")

process_symmetry("r3,r1,r0")
