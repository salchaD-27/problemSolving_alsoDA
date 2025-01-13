from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bits = len(bin(max(candidates))) - 2
        res = 0
        for i in range(max_bits):
            count = 0
            for num in candidates:
                if num & (1 << i): count += 1
            res = max(res, count)
        return res