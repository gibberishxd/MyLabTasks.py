import math

print("Enter height ")
h = input()
print("Enter Radius ")
r = input()

S = int(math.pi) * int(r) ** 2 * int(h)
r = S / 3

print("Volume of Cylinder", S)
print("Volume of Cone", r)
