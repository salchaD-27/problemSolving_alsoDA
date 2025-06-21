# class Solution:
#     def minimumDeletions(self, word: str, k: int) -> int:
#         freqMap={}
#         for i in range(len(word)):
#             if word[i] not in freqMap: freqMap[word[i]]=1
#             else: freqMap[word[i]]+=1
#         minFreq=float('inf')
#         for char in freqMap:
#             minFreq=min(minFreq,freqMap[char])
#         maxPossFreq=k+minFreq
#         removes=0
#         for char in freqMap:
#             if freqMap[char]>maxPossFreq: removes+=freqMap[char]-maxPossFreq
#         return removes

from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        res = float('inf')
        for i in range(len(freq)):
            deletions = 0
            target = freq[i]  # all freq [target, target + k]
            for f in freq:
                if f < target: deletions += f
                elif f > target + k: deletions += f - (target + k)
            res = min(res, deletions)
        return res