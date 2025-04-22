# class Solution:
#     def findSubstringInWraproundString(self, s: str) -> int:
#         base = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
#         count = 0
#         L = 0
#         n = len(s)
#         substrings = set()
#         while L < n:
#             R = L
#             while R < n and (ord(s[R]) - ord(s[R-1]) == 1 or (s[R-1] == 'z' and s[R] == 'a')):
#                 if s[L:R+1] not in substrings:
#                     substrings.add(s[L:R+1])
#                     count += 1
#                 R += 1
#             L += 1
#         return count
    
# class Solution:
#     def findSubstringInWraproundString(self, s: str) -> int:
#         dp = [0] * 26
#         count = 0
#         for i in range(len(s)):
#             if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i] == 'a')): dp[ord(s[i]) - ord('a')] = dp[ord(s[i-1]) - ord('a')] + 1
#             else: dp[ord(s[i]) - ord('a')] = 1
#             count += dp[ord(s[i]) - ord('a')]        
#         return count

from collections import defaultdict
class Solution(object):
    def findSubstringInWraproundString(self, s):
        counts = defaultdict(int)
        max_len = 0
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1: max_len += 1
            else: max_len = 1
            counts[s[i]] = max(counts[s[i]], max_len)
        return sum(counts.values())