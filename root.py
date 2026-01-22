def mySqrt(x):
    root = 0
    i = 1
    while x >= i:
        root += 1
        x -= i
        i += 2
    return root


print(mySqrt(int(input())))