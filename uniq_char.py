def firstUniqChar(s):
    count = {}
    for i in s:
        if i not in count:
            count[i] = 0
        else:
            count[i] += 1
    for i in count:
        if count[i] == 0:
            return s.index(i)
    return -1



print(firstUniqChar(input()))