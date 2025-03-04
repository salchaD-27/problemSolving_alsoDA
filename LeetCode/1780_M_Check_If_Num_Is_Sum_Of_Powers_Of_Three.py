class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(remN, power):
            if remN == 0: return True
            if 3 ** power > remN: return False
            return backtrack(remN - 3 ** power, power + 1) or backtrack(remN, power + 1)
        return backtrack(n, 0)
    
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2: return False
            n //= 3
        return True