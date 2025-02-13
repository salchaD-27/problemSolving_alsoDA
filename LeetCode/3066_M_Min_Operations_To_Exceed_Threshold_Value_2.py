# from typing import List
# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         ops = 0
#         nums.sort()
#         while len(nums) > 1 and nums[0] < k:
#             first = nums.pop(0)
#             second = nums.pop(0)
#             new_element = first + 2 * second
#             nums.append(new_element)
#             nums.sort()
#             ops += 1
#         return ops

import heapq
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) 
        ops = 0
        while len(nums) > 1 and nums[0] < k:
            a = heapq.heappop(nums) 
            b = heapq.heappop(nums) 
            new_element = min(a, b) * 2 + max(a, b)
            heapq.heappush(nums, new_element) 
            ops += 1 
        return ops