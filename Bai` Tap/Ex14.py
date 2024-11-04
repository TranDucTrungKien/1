from math import sqrt
def PTB2(a,b,c):

    a = float(input("Nhap a="))
    b = float(input("Nhap b="))
    c = float(input("Nhap c="))
    if a==0:
        if b != 0:
            x = -c / b
            print("Nghiem la x", x)
        else:
            if c == 0:
                print("phuong trinh vo so N0")
            else:
                print("phuong trinh vo N0")
    else:
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/(2*a)
            x2=(-b-sqrt(D))/(2*a)
            print("Phuong trinh co 2 nghiem phan biet",x1,"và",x2)
        if D==0:
            x=(-b/(2*a))
            print("Phuong trinh co nghiem kep",x)
        if D<0:
            print("Phuong trinh vo nghiem")
