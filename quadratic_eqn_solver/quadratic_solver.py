import math

# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    # Two real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real roots: ", root1, root2)
    
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print("One real root: ", root)

else:
    # Complex roots
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imag_part}i")
    print(f"Root 2: {real_part} - {imag_part}i")