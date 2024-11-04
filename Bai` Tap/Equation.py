import math


def ptb1(a,b):
    if a==0 and b==0:
        return "Infinity"
    elif a==0 and b!=0:
        return "No Solution"
    else:
        x=-b/a
        return x
def ptb2(a,b,c):
    if a==0:
        return ptb1(b,c)
    else:
        delta=math.pow(b,2)-4*a*c
        if delta<0:
            return "No Solution"
        elif delta==0:
            return (-b/(2*a))
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2 * a)
            result=f"x1={x1};x2={x2}"
            return result
