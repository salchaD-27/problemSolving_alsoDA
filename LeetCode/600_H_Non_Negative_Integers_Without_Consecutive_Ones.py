# 1: 0/1
# 2: 10
# 3: 100/101
# 4: 1000/1001/1010
# 5: 10000/10001/10010/10100/10101

class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [0] * 32
        fib[0], fib[1] = 1, 2
        for i in range(2, 32):
            fib[i] = fib[i-1] + fib[i-2]
        prev_bit = 0
        result = 0
        for i in range(30, -1, -1):
            if (n & (1 << i)):
                result += fib[i]
                if prev_bit == 1: return result
                prev_bit = 1
            else: prev_bit = 0
        return result + 1