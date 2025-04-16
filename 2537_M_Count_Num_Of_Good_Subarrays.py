from typing import List
from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        pair_count = 0
        result = 0
        for right in range(len(nums)):
            val = nums[right]
            pair_count += count[val]
            count[val] += 1
            while pair_count >= k:
                result += len(nums) - right
                pair_count -= count[nums[left]] - 1
                count[nums[left]] -= 1
                left += 1
        return result