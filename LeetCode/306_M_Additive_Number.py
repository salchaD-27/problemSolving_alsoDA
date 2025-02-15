class Solution:
    def isValid(self, a: int, b: int, remaining: str) -> bool:
        while remaining:
            c = a + b
            c_str = str(c)
            if not remaining.startswith(c_str): return False
            remaining = remaining[len(c_str):]
            a, b = b, c
        return True
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'): continue
                a, b = int(num1), int(num2)
                if self.isValid(a, b, num[j:]): return True
        return False