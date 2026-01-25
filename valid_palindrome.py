def isPalindrome(s):
    string = ""
    s = s.lower()
    for i in s:
        if (ord(i) > 96 and ord(i) < 123) or (ord(i) > 47 and ord(i) < 58):
            string += i
    if string == string[::-1]:
        return True
    return False


print(isPalindrome(input()))