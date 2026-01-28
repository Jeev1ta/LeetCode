def binary(num, count):
    if num == 1:
        return count
    if (num % 2 != 0):
        count += 1
    return binary(num // 2, count)

def hammingWeight(n):
    return binary(n, 0) + 1



print(hammingWeight(int(input())))