import math

#Обчислити об'єми циліндра і конуса, що мають однакову висоту H і однаковий радіус основи R

print("Enter height ")
h = input()
print("Enter Radius ")
r = input()

S = float(math.pi) * float(r) ** 2 * float(h)
r = S / 3

print("Volume of Cylinder", S)
print("Volume of Cone", r)
