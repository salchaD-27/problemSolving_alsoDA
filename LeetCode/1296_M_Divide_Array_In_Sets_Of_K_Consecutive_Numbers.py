from collections import Counter
class Solution:
    def isPossibleDivide(self, A, k):
        c = Counter(A)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0: return False
        return True