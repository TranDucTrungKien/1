n=int(input("input n:"))
count=0
for i in range(1,n+1):
    r=n%i
    if r ==0:
        count=count+1
if count==2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")