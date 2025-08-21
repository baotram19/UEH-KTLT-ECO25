import math

# Nhập hệ số a, b, c
a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print("Unlimited solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    # Phương trình bậc 1: bx + c = 0
    x = -c / b
    print(f"x1={x:.2f}")
else:
    # Phương trình bậc 2
    delta = b**2 - 4*a*c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        x = -b / (2*a)
        print(f"x1={x:.2f}")
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"x1={x1:.2f}, x2={x2:.2f}")
