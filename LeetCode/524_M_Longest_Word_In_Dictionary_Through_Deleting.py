# from typing import List
# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:    
#         def longestCommonSubsequence(text1, text2):
#             prev = [0] * (len(text2) + 1)
#             for i in range(1, len(text1) + 1):
#                 curr = [0] * (len(text2) + 1)
#                 for j in range(1, len(text2) + 1):
#                     if text1[i - 1] == text2[j - 1]: curr[j] = prev[j - 1] + 1
#                     else: curr[j] = max(prev[j], curr[j - 1])
#                 prev = curr 
#             lcs = []
#             i, j = len(text1), len(text2)
#             while i > 0 and j > 0:
#                 if text1[i - 1] == text2[j - 1]:
#                     lcs.append(text1[i - 1])
#                     i -= 1
#                     j -= 1
#                 elif prev[j] == prev[j - 1]: j -= 1
#                 else: i -= 1
#             return prev[len(text2)], ''.join(reversed(lcs))

#         res=[]
#         temp=0
#         for word in dictionary:
#             tempLen,subSeq=longestCommonSubsequence(s, word)
#             if(tempLen>temp):
#                 temp=tempLen
#                 res=[subSeq]
#             if(tempLen==temp):
#                 res.append(subSeq)
#         res.sort()
#         return res[0]

# from typing import List
# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:    
#         def longestCommonSubsequence(text1, text2):
#             prev = [0] * (len(text2) + 1)
#             for i in range(1, len(text1) + 1):
#                 curr = [0] * (len(text2) + 1)
#                 for j in range(1, len(text2) + 1):
#                     if text1[i - 1] == text2[j - 1]: curr[j] = prev[j - 1] + 1
#                     else: curr[j] = max(prev[j], curr[j - 1])
#                 prev = curr
#             return prev[len(text2)]

#         result = ""
#         max_len = 0
#         for word in dictionary:
#             if longestCommonSubsequence(s, word) == len(word):
#                 if len(word) > max_len or (len(word) == max_len and word < result):
#                     result = word
#                     max_len = len(word)
#         return result

from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(s, word):
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]: j += 1
                i += 1
            return j == len(word)
        result = ""
        
        for word in dictionary:
            if isSubsequence(s, word):
                if len(word) > len(result) or (len(word) == len(result) and word < result): result = word
        return result