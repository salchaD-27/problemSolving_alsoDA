from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def count_pairs(max_dist: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k: low = mid + 1
            else: high = mid
        return low