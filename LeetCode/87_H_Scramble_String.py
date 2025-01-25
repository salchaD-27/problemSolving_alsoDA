from typing import Dict
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def divide(s1: str, s2: str) -> bool:
            if s1 == s2: return True
            if sorted(s1) != sorted(s2): return False
            if (s1, s2) in memo: return memo[(s1, s2)]
            n = len(s1)
            for i in range(1, n):
                if (divide(s1[:i], s2[:i]) and divide(s1[i:], s2[i:])) or \
                    (divide(s1[:i], s2[-i:]) and divide(s1[i:], s2[:-i])):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False
        return divide(s1, s2)