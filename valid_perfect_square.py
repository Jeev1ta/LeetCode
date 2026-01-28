def isPerfectSquare(num):
    if num ** 0.5 == int(num ** 0.5):
        return True
    return False


print(isPerfectSquare(int(input())))