from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        temp = {}
        for key, val in nums1:
            temp[key] = temp.get(key, 0) + val
        for key, val in nums2:
            temp[key] = temp.get(key, 0) + val
        return sorted([[key, val] for key, val in temp.items()])