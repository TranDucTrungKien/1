def draw_odd_matrix(n):
    if n % 2 == 0 or n<8:
        print("The matrix level is even. Please provide an odd level.")
        return
    center = n // 2
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0) or (i == 0 and j == n - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == n - 1):
                print("1", end=" ")  # Góc là '1'
            elif i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("x", end=" ")
            elif (i == center and j == center):
                print("0", end=" ")
            elif (abs(i - center) <= 1 and abs(j - center) <= 1):
                print("*", end=" ")
            elif i == j or i + j == n - 1:
                print("1", end=" ")
            else:
                print(" ", end=" ")
        print()
n = 9
draw_odd_matrix(n)
print(" ")
def draw_custom_pattern(size):
    if size % 2 != 0 or size < 6:
        print("Please enter an even size that is at least 6.")
        return
    start = size // 2 - 1
    end = size // 2
    for i in range(size):
        for j in range(size):
            if start <= i <= end and start <= j <= end:
                print("1", end=" ")
            elif (start - 1 <= i <= end + 1) and (start - 1 <= j <= end + 1):
                print("@", end=" ")
            elif i == j or i + j == size - 1:
                print("0", end=" ")
            elif i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
draw_custom_pattern(14)