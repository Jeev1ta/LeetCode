def removeElement(nums, val):
    pos = 0
    for i in nums:
        if i != val:
            nums[pos] = i
            pos += 1
    return pos


nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))