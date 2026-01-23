class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = (len(a) - len(b))* '0' + b
        else:
            a = (len(b) - len(a))* '0' + a
        carry = '0'
        sum1 = ''
        for i in range(len(b)-1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry == '1':
                    sum1 += '1'
                    carry = '1'
                else:
                    sum1 += '0'
                    carry = '1'
            elif a[i] == '1' and b[i] == '0':
                if carry == '1':
                    sum1 += '0'
                    carry = '1'
                else:
                    sum1 += '1'
                    carry = '0'
            elif a[i] == '0' and b[i] == '1':
                if carry == '1':
                    sum1 += '0'
                    carry = '1'
                else:
                    sum1 += '1'
                    carry = '0'
            if a[i] == '0' and b[i] == '0':
                if carry == '1':
                    sum1 += '1'
                    carry = '0'
                else:
                    sum1 += '0'
                    carry = '0'
        if carry == '1':
            return (carry + sum1[::-1])
        return (sum1[::-1])