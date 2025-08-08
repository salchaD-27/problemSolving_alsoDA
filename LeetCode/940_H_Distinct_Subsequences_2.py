from collections import Counter
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        res, end = 0, Counter()
        for c in s:
            res, end[c] = res * 2 + 1 - end[c], res + 1
        return res % (10**9 + 7)
    
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] * 26
        for c in s:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)