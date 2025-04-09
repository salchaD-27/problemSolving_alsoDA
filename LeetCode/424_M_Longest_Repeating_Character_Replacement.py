# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         L = R = res = 0
#         tempK = k
#         while R < len(s): 
#             if s[R] == s[L]: 
#                 R += 1
#             elif tempK > 0: 
#                 R += 1
#                 tempK -= 1
#             else: 
#                 L += 1
#                 tempK = k 
#             res = max(res, R - L)
#         return res

from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        max_freq = 0
        count = Counter() 
        res = 0 
        for R in range(len(s)):
            count[s[R]] += 1
            max_freq = max(max_freq, count[s[R]])
            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res