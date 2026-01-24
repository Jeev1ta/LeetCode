def isValid(s):
    lst = []
    for i in s:
        if i in '([{':
            lst.append(i)
        else:
            if len(lst) > 0:
                if i == ']' and lst[-1] != '[':
                    return False
                elif i == '}' and lst[-1] != '{':
                    return False
                elif i == ')' and lst[-1] != '(':
                    return False
                else:
                    lst.pop(-1)
            elif len(lst) == 0 and i in '}])':
                return False
    if len(lst) != 0:
        return False
    return True




print(isValid(input()))