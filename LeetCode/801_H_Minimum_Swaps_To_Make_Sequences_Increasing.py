# from typing import List
# class Solution:
#     def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
#         nums1Violating, nums2Violating=[],[]
#         if not nums1[0]<nums1[1]: nums1Violating.append(0)
#         if not nums2[0]<nums2[1]: nums2Violating.append(0)
#         for i in range(1, len(nums1)-1):
#             if not nums1[i-1]<nums1[i]<nums1[i+1]: nums1Violating.append(i)
#             if not nums2[i-1]<nums2[i]<nums2[i+1]: nums2Violating.append(i)
#         if not nums1[-2]<nums1[-1]: nums1Violating.append(len(nums1)-1)
#         if not nums2[-2]<nums2[-1]: nums2Violating.append(len(nums2)-1)
#         return 

from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep = [float('inf')] * n
        swap = [float('inf')] * n
        keep[0] = 0
        swap[0] = 1
        for i in range(1, n):
            # no swap at i and i-1
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            # swap at i or i-1
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1] + 1)
        return min(keep[-1], swap[-1])