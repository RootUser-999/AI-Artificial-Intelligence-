x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))  # Changed from y1 to x3 for consistency

if x1 > x2 and x1 > x3:
    print("x1 is the largest number")
elif x2 > x1 and x2 > x3:
    print("x2 is the largest number")
else:
    print("x3 is the largest number")