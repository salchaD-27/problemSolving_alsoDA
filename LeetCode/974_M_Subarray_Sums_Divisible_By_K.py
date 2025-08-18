# from typing import List
# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         count = 0
#         n = len(nums)
#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 if curr_sum % k == 0: count += 1
#         return count

from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0: mod += k
            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else: prefix_map[mod] = 1
        return count