#     0 1 1 1 1 1  0  0  0
#    -1 1 1 1 1 1 -1 -1 -1
# dp -1 0 1 2 3 4  3  2  1

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_length = 0
        prefix_map = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += -1 if num == 0 else 1
            if prefix_sum in prefix_map:
                length = i - prefix_map[prefix_sum]
                max_length = max(max_length, length)
            else: prefix_map[prefix_sum] = i
        return max_length