def shape2(n):
    i=0
    while i<n:
        j=0
        while j<n:
            if i+j>=n-1:
                print("*",end='')
            else:
                print(" ",end='')
            j=j+1
        i=i+1
        print()
        i=i+1
shape2(7)
