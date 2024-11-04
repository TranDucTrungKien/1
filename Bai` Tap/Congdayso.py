#S=1+2+3...+N
n=int(input('Enter N: '))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print('S=',s)