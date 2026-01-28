def findTheDifference(s, t):
    for i in t:
        if len(s) == 0:
            return i
        if i not in s:
            return i
        s = s.replace(i, '', 1)



print(findTheDifference(input(), input()))