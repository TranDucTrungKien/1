def func(m,n,a,b):
    s1=s2=0
    for i in range(m,n,1):
        if i%3==0:
            break
        else:
            s1=s1+a+b
        if a <= i <= b and i%2 == 0:
            s2 = s2 + i
    return s1, s2
print(func(1,5,3,10))