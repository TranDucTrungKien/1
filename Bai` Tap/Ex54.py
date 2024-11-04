import math
def calculate_perimeter(r):
    return 2 * math.pi * r
def calculate_area(r):
    return math.pi * r ** 2
try:
    r = float(input("Please enter the radius: "))
    perimeter = calculate_perimeter(r)
    area = calculate_area(r)
    print("Perimeter =", perimeter)
    print("Area =", area)
except ValueError:
    print("Error! Please enter a valid number.")