n = int(input('Enter the n(th) fibonacci: '))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        pre_num = 1
        cur_num = 1
        for _ in range(2, n):
            next_num = pre_num + cur_num
            pre_num = cur_num
            cur_num = next_num
        return cur_num
print(f'The fibonacci {n} is {fibonacci(n)}.')

def fibonacci_list(n):
    for i in range(1, n+1):
        print(fibonacci(i), end=' ')
fibonacci_list(n)