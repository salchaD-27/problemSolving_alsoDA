# from typing import List
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         L = R = 0
#         res = []
#         n = len(s)
#         len_p = len(p)
#         while R < n:
#             window = s[L:R+1]
#             if R - L + 1 < len_p:
#                 R += 1
#             elif sorted(window) == sorted(p):
#                 res.append(L)
#                 L += 1
#                 R = L
#             else:
#                 L += 1
#                 R = L
#         return res

from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k: return []
        p_count = Counter(p)
        window_count = Counter()
        res = []
        for i in range(n):
            window_count[s[i]] += 1
            if i >= k:
                if window_count[s[i - k]] == 1: del window_count[s[i - k]]
                else: window_count[s[i - k]] -= 1
            if window_count == p_count: res.append(i - k + 1)
        return res