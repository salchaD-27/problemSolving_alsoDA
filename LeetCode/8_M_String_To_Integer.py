class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0: return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for i in range(len(s)):
            if s[i].isdigit(): result = result * 10 + int(s[i])
            else: break
        result *= sign
        if result < -2**31: return -2**31
        elif result > 2**31 - 1: return 2**31 - 1
        return result