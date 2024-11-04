N=5
for i in range(N+1,1,-2):
    for j in range(0,i,1):
        print(f"{i}+{j}={i+j}", end="\t")
    print()
    