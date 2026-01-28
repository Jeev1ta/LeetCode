def recursive_add(num):
    if num < 10:
        return num
    return recursive_add(num//10 + num % 10)

print(recursive_add(int(input())))