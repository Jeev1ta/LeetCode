def singleNumber(nums):
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1    
    for j in count:
        if count[j] == 1:
            return j
        

print(singleNumber(list(map(int, input().split()))))