import math

print("Enter the coefficient a: ")
x = input()
a = float(x)

print("Enter the coefficient b: ")
y = input()
b = float(y)

print("Enter the coefficient c: ")
z = input()
c = float(z)

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are:", root1, "and", root2)
    
elif discriminant == 0:
    root = -b/(2 * a)
    print("The equation has repeated real roots", root)
else:
    print("The equation has complex roots")

