import math
a = int(input())
b = int(input())
c = int(input())

#x = a*x**2 + b*x + c

D = b**2 - 4*a*c

if D < 0:
    print ("x nenáleží v R")
elif D==0:
    x = -b / (2*a)
    print ("x = ", x)
else:
    x = (-b + math.sqrt(D))/ (2*a)
    y = (-b - math.sqrt(D))/ (2*a)
    print("x1 = ", x)
    print("x2 = ", y)


