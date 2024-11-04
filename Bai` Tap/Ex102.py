def shape1(n):
    i=0
    while i<n:
        j=0
        while j<n:
            if j==0 or j==n-1 or i==0 or i==n-1:
                print("*",end='')
            else:
                print(" ",end='')
            j=j+1
        print()
        i=i+1
shape1(7)