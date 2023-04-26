l1 = [1,2,3,4,5,6,7,8,9]


cislo = 6
i = 0
j = len(l1) 

while i <= j:

    stred = (i + j) // 2

    if cislo == l1[stred]:
        print(stred)
        break
    
    elif cislo < l1[stred]:
        j = stred - 1
    elif cislo > l1[stred]:
        i = stred + 1




    
        
        
