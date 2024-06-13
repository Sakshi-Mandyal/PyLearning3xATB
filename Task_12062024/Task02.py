# Program to classifies a triangle based on its side lengths

side1 = input("Enter side 1: ")
side2 = input("Enter side 2: ")
side3 = input("Enter side 3: ")
if side1 == side2 == side3:
    print("This is an Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an Isosceles Triangle")
else:
    print("This is an Scalene Triangle")