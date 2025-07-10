# from typing import List
# from collections import Counter
# class Solution:
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#         targetFreq=list(Counter(pattern).values())
#         res=[]
#         for word in words:
#             tempFreq=list(Counter(word).values())
#             if tempFreq==targetFreq: res.append(word)
#         return res

from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            if len(word) != len(pattern): return False
            w2p, p2w = {}, {}
            for w, p in zip(word, pattern):
                if w in w2p and w2p[w] != p: return False
                if p in p2w and p2w[p] != w: return False
                w2p[w] = p
                p2w[p] = w
            return True
        return [word for word in words if match(word, pattern)]