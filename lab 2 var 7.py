import math
from sys import exit

print("Enter coordinate for x")
x = input()

print("Enter coordinate for y")
y = input()

r = math.sqrt(float(x)*float(x) + float(y)*float(y))

a: float = 0

if r <= 1:
    a = math.atan(float(y) / float(x))
    
else:
    print("Coordinate is not included")
    exit()


if a <= 1 / 4 * float(math.pi) and a <= 1 / 2 * math.pi or 3 / 4 * float(math.pi) < a and a < float(math.pi) or 5 / 4 * float(math.pi) < a and a < 3 / 2 * float(math.pi) or 7 / 4 * float(math.pi) <= a and a <= 2 * float(math.pi):
    print("Coordinate is included")

else:
    print("Coordinate is not included")