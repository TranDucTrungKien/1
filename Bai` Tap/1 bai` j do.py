def solutionFirstDegree(a,b):
    if a==0 and b==0:
        return "Infinity"
    elif a==0 and b!=0:
        return "No Solution"
    else:
        x=-b/a
        return x
#0x+0
test1=solutionFirstDegree(0,0)
print("0x+0=0")
print(test1)

#0x+0
test2=solutionFirstDegree(0,3)
print("0x+3=0")
print(test2)

#tinh GPA
def calcGPA(qt,gk,ck):
    avg=qt*0.3+gk*0.2+ck*0.5
    return avg

