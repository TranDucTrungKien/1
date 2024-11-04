print('Enter a number [1:10]')
x=-1
while x<1 or x>10:
    x=int(input('Enter a number [1:10]: '))
print(x**2)