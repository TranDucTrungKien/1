def shape2(n):
    i=0
    while i<n:
        j=0
        while j<n:
            if i<=j<=n-1-i:
                print("*",end=' ')
            elif i>=j>=n-1-i:
                print("*", end=' ')
            else:
                print(" ",end=' ')
            j+=1
        i+=1
        print()
shape2(8)
