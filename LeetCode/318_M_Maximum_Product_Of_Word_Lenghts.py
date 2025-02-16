# from typing import List
# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#         ans=0
#         for i in range(len(words)):
#             temp1=list(words[i])
#             for j in range(i+1, len(words)):
#                 temp2=list(words[j])
#                 if(not list(set(temp2).intersection(set(temp1)))): ans=max(ans, len(words[i])*len(words[j]))
#         return ans

from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lengths = [len(word) for word in words]
        for i, word in enumerate(words):
            for char in word:
                bitmasks[i] |= 1 << (ord(char) - ord('a'))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0: ans = max(ans, lengths[i] * lengths[j])        
        return ans