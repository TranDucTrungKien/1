def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
#Case 1
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())
main()
#Case 2
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())
main()
#Case 3
def main():
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())
main()