def test(n):
    sum = 0
    for i in range(1, n):
        r = n % i
        if r == 0:
            sum += i
    return sum

# perfect number
def perfect():
    if test(n) == n:
        return f'{n} is perfect number'
    else:
        return f'{n} is not perfect number'

n = int(input('Input n:'))
print(perfect())

# abundant number
def abundant():
    if test(n) > n:
        return f'{n} is abundant number'
    else:
        return f'{n} is not abundant number'

n = int(input('Input n:'))
print(abundant())

# deficient number
def deficient():
    if test(n) < n:
        return f'{n} is deficient number'
    else:
        return f'{n} is not deficient number'

n = int(input('Input n:'))
print(deficient())
