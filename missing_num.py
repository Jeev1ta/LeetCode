def missingNumber(nums):
    nums.sort()
    for i in range(len(nums) + 1):
        if i not in nums:
            return i

#or

def missingNumber_1(nums):
    n = len(nums)
    total = n*(n+1)//2
    total_num = sum(nums)
    return total - total_num

nums = list(map(int, input().split()))

print(missingNumber(nums))
print(missingNumber_1(nums))