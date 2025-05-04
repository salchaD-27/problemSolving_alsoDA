from typing import List
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for domino in dominoes:
            domino.sort()
            count[tuple(domino)] += 1
        pairs = 0
        for freq in count.values():
            if freq > 1: pairs += (freq * (freq - 1)) // 2
        return pairs