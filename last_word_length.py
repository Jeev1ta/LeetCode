def lengthOfLastWord(s):
    s1 = s.split()
    return(len(s1[-1]))


print(lengthOfLastWord(input()))