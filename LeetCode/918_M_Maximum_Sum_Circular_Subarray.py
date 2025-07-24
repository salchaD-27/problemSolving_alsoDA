from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        def kadane_max(arr):
            curr = max_sum = arr[0]
            for num in arr[1:]:
                curr = max(num, curr + num)
                max_sum = max(max_sum, curr)
            return max_sum
        def kadane_min(arr):
            curr = min_sum = arr[0]
            for num in arr[1:]:
                curr = min(num, curr + num)
                min_sum = min(min_sum, curr)
            return min_sum
        max_kadane = kadane_max(nums)
        min_kadane = kadane_min(nums)
        if max_kadane < 0: return max_kadane
        return max(max_kadane, total - min_kadane)