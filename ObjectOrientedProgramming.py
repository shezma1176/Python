import math

# Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print("\nRectangle:")
print("Area =", rectangle_area)
print("Perimeter =", rectangle_perimeter)

# Circle
radius = float(input("\nEnter the radius of the circle: "))

circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius

print("\nCircle:")
print("Area =", circle_area)
print("Circumference =", circle_circumference)


