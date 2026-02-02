class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        else:
            num1 = '0'*(len(num2) - len(num1)) + num1
        carry = 0
        sum1 = []
        for i in range(len(num1)-1, -1, -1):
            sum1.append(str((((ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0'))) + carry) % 10))
            carry = (((ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0')))+carry) // 10
        if carry != 0:
            sum1.append(str(carry))
        return ''.join(reversed(sum1))