class Solution:
    def integerReplacement(self, n: int) -> int:
        def recur(remN, opers):
            if remN == 1: return opers
            if remN % 2 == 0: return recur(remN // 2, opers + 1)
            return min(recur(remN - 1, opers + 1), recur(remN + 1, opers + 1))
        return recur(n, 0)

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0: n //= 2  
            elif n == 3 or (n & 3) == 1: n -= 1  
            else: n += 1  
            count += 1  
        return count