class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1')
        res = 0
        for i in reversed(range(32)):
            if num1 & (1 << i):
                if count > 0:
                    res |= (1 << i)
                    count -= 1
        for i in range(32):
            if not (res & (1 << i)) and count > 0:
                res |= (1 << i)
                count -= 1
        return res