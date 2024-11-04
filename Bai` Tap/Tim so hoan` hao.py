n=int(input("input n:"))
sum=0
for i in range(1,n):
    r= n%i
    if r==0:
        sum=sum+i
if sum==n:
    print(n,"is a perfect number")
else:
    print(n, "is a not perfect number")