#Bai cua Nhat
n=int(input("Input n:"))
s=0
i=1
while i<=n:
    s=s+i/(i+1)
    i=i+1
print(f"S({n})={s}")

#Bai` cua L Thinh
n=int(input("Input n:"))
if n>=0:
    sum=0
    i=1
    while i<=n:
        s=i/(i+1)
        sum=sum+s
        i=i+1
    print(f"S({n})={sum}")
else:
    print("Input tao lao")