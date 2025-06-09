from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) % 2 == 1:
            for a in nums1:
                res ^= a
        if len(nums1) % 2 == 1:
            for b in nums2:
                res ^= b
        return res