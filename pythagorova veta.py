import math
a= int(input("Odvěsna a ",))
b= int(input("Odvěsna b ",))
c= int(input("Přepona c ",))

if a == 0:
    a = math.sqrt(c**2 - b**2)
    print ("Odvěsna a má délku ",a)
elif b == 0:
    b = math.sqrt(c**2 - a**20)
    print ("Odvěsna a má délku ",b)
else:
    c = math.sqrt(a**2 + b**2)
    print ("Přepona c má délku ",c)
                  





