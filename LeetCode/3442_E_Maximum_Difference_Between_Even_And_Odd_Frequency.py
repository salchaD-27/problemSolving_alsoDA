from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        maxA1, minA2=0, float('inf')
        for freq in list(count.values()):
            if freq%2==0: minA2=min(minA2, freq)
            else: maxA1=max(maxA1, freq)
        return maxA1-minA2