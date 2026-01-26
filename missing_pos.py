def firstMissingPositive(nums):
    nums.sort()
    smallest = 1
    for i in nums:
        if i == smallest:
            smallest += 1
    return smallest



print(firstMissingPositive(list(map(int, input().split()))))