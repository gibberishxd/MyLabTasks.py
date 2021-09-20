import math
import sys

#Обчислити об'єми циліндра і конуса, що мають однакову висоту H і однаковий радіус основи R

print("Enter height ")
h = input()
print("Enter Radius ")
r = input()

if float(h) <= 0:
    print("Height can't be zero or less")
    sys.exit()
if float(r) <= 0:
    print("Radius can't be zero or less")
    sys.exit()


S = float(math.pi) * float(r) ** 2 * float(h)
r = S / 3

print("Volume of Cylinder", S)
print("Volume of Cone", r)
