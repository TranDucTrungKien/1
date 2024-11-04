N=5
S=0
for i in range (N+1,1,-1):
    if i%2==0:
        continue
    else:
        for j in range (0,i,2):
            S=S+i
print(S)
'''
for 1: 6->2
[1]:i=6
check i%2==0 <-> 6%2==0 ->T
-> continue
[2]:i=5
check i%2==0 <-> 5%2==1 ->F
    for 2

'''