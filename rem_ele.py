def removeElement(nums, val):
    pos = 0
    for i in nums:
        if i != val:
            nums[pos] = i
            pos += 1
    return pos


nums = map(int, input().split())
val = int(input())
print(removeElement(nums,val))