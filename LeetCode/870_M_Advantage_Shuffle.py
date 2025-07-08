#       nums2 = [1,10,4,11]
#       nums1 = [2,7,11,15]
# sortednums2 = [1,4,10,11]
# sortednums1 = [2,7,11,15]
# 11->15, 10->11, 4->7, 1->2
#   orignums2 = [1,10,4,11]
#  finalnums1 = [2,7,11,15]
# from typing import List
# class Solution:
#     def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums2IdxMap={i:nums2[i] for i in range(len(nums2))}
#         nums1.sort()
#         nums2.sort()
#         advantageMap={nums2[i]:nums1[i] for i in range(len(nums1))}
#         return [advantageMap[nums2IdxMap[num]] for num in nums2IdxMap]

import heapq
from typing import List
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        # nums2maxheap (val,idx)
        max_heap = [(-val, i) for i, val in enumerate(nums2)]
        heapq.heapify(max_heap)
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        while max_heap:
            val, i = heapq.heappop(max_heap)
            val = -val
            if nums1[right] > val:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        return res