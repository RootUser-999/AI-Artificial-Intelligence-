x1 = float(input("Enter point x1: "))
x2 = float(input("Enter point x2: "))
y1 = float(input("Enter point y1: "))
y2 = float(input("Enter point y2: "))

distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

print(f"The distance of the points is {distance}")