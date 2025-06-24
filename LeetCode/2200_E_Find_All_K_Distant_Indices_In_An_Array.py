from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        targetIdxs = [i for i in range(len(nums)) if nums[i] == key]
        res = set()
        for i in range(len(nums)):
            for idx in targetIdxs:
                if abs(i - idx) <= k:
                    res.add(i)
                    break
        return sorted(res)