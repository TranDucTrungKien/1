def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_prime_numbers(N):
    return ', '.join(str(n) for n in range(1, N + 1) if is_prime(n))
def list_even_numbers(N):
    return ', '.join(str(n) for n in range(1, N+1) if n % 2 == 0)
def list_odd_numbers(N):
    return ', '.join(str(n) for n in range(1, N+1) if n % 2 != 0)

