from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res1=[words[0]]
        lastBin=groups[0]
        for i in range(1, len(words)):
            if(groups[i]!=lastBin):
                lastBin=groups[i]
                res1.append(words[i])
        res2=[]
        lastBin=groups[0]
        for i in range(1, len(words)):
            if(groups[i]!=lastBin):
                lastBin=groups[i]
                res2.append(words[i])
        return res1 if len(res1)>len(res2) else res2