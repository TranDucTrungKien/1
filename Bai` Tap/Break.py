n=int(input('Enter N: '))
s=0
for i in range(1,n+1):
    s+=i
    if s>=15:
        break
print('S=',s)