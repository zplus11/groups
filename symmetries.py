from time import sleep
import sys

print("Welcome. Here you can calculate function compositions of symmetries of regular polygons.")
sides = input("To begin with, provide the number of sides in your regular polygon: ")
if sides.isdigit():
    sides = int(sides)
    if sides > 2:
        if sides%2 == 0:
            nature = "e"
        else:
            nature = "o"
    else:
        print("Error. Provide integer (>2) number of sides.")
        sleep(3)
        sys.exit()
else:
    print("Error. Couldn't convert to integer >2")

print(f"The polygon you have provided is of {sides} sides. Now there are following permissible operations:")
if nature == "e":
    for i in range(sides):
        print("r{0}: anti-clockwise rotation of {1} degrees".format(i, i*360/sides))
    for i in range(int(sides/2)):
        print("d{0}: reflection about vertex {1}".format(i, i + 1))
    for i in range(int(sides/2)):
        print("f{0}: reflection about axis between vertices {1} and {2}".format(i, i + 1, i + 2))
