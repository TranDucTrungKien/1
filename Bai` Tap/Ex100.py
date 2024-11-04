import math

def can_long_can(n):
    result=0
    for i in range(n,0,-1):
        result= math.sqrt(i+result)
    return result
n = int(input("Dua bo m so n: "))
print(f"Ket qua may can tim la n={n} : {can_long_can(n)}")