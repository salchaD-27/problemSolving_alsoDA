from itertools import groupby
from collections import Counter
class Solution:
    def maxRepOpt1(self, S):
        A = [[c, len(list(g))] for c, g in groupby(S)]
        count = Counter(S)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1: res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res