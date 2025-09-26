from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return [i & 1 ^ (seq[i] == '(') for i, c in enumerate(seq)]

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        res = n * [0]
        
        cnt1, cnt2 = 0, 0
        for i in range(n):
            ch = seq[i]
            if ch == '(':
                if cnt2 > cnt1: cnt1 += 1
                else:
                    cnt2 += 1
                    res[i] = 1
            else:
                if cnt1 > cnt2: cnt1 -= 1
                else:
                    res[i] = 1
                    cnt2 -= 1
        return res