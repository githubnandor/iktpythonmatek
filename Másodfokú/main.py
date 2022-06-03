import math

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b * b - 4 * a * c
x1 = (-1 * b + math.sqrt(delta)) / 2 * a
x2 = (-1 * b - math.sqrt(delta)) / 2 * a

print("Megoldás: X1: ", x1)
print("Megoldás: X2: ", x2)