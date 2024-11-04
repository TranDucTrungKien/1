def input_valid_value():
    try:
        n=int(input('Enter n>=0: '))
        if n<0:
            return False
        return n
    except:
        return False
def strtobool(ask):
    return ask in ('y','y')
def S36(n):
    i=1
    sum=0
    while i<=n:
        sum= sum+1/(i*(i+1))
        i=i=1
        return sum
    n=3
    print(f'S({n}){S36(n)}=')
while True:
    n=input_valid_value()
    if n!=False:
        print(f'S({n})={S36(n)}')
        ask=input('Continue(y/n)?:')
        result=strtobool(ask)
        if result==False:
            print('Cut')
            break

def factorial(n):
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i=i+1
    return fact
def S40(n):
    i=1
    s=0
    while i<=n:
        s=s+factorial(i)
        i=i+1
    return s
n=3
print(f'S({n})={S40(n)}')