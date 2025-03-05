# from collections import Counter
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         res=0
#         for i in range(len(s)):
#             count=Counter(s[:i+1])
#             if(min(list(count.values()))>=k): res=max(res,i+1)
#         return res

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        count = Counter(s)
        for ch in count:
            if count[ch] < k: return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)