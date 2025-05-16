# from typing import List
# class Solution:
#     def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
#         res1=[words[0]]
#         lastBin=groups[0]
#         for i in range(1, len(words)):
#             if(groups[i]!=lastBin):
#                 lastBin=groups[i]
#                 res1.append(words[i])
#         res2=[]
#         lastBin=groups[0]
#         for i in range(1, len(words)):
#             if(groups[i]!=lastBin):
#                 lastBin=groups[i]
#                 res2.append(words[i])
#         return res1 if len(res1)>len(res2) else res2

class Solution(object):
    def differByOneChar(self, word1, word2):
        if len(word1) != len(word2): return False
        diffCount = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2: diffCount += 1
        return diffCount == 1
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(groups)
        dp = [1] * n
        parent = [-1] * n
        maxi = 0
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and \
                   self.differByOneChar(words[i], words[j]) and \
                   dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > maxi: maxi = dp[i]
        result = []
        for i in range(n):
            if dp[i] == maxi:
                while i != -1:
                    result.append(words[i])
                    i = parent[i]
                break
        return result[::-1]