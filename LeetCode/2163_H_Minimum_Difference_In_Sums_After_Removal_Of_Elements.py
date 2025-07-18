import heapq
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n
        # prefix, min sum of n largest, from left
        left_sum = [0] * (total_len)
        max_heap = []
        left_total = sum(nums[:n])
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
        left_sum[n - 1] = left_total
        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_total += nums[i]
            left_total += heapq.heappop(max_heap)
            left_sum[i] = left_total
        # suffix: max sum of n smallest, from right
        right_sum = [0] * (total_len)
        min_heap = []
        right_total = sum(nums[-n:])
        for i in range(total_len - 1, total_len - n - 1, -1):
            heapq.heappush(min_heap, nums[i])
        right_sum[total_len - n] = right_total
        for i in range(total_len - n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_total += nums[i]
            right_total -= heapq.heappop(min_heap)
            right_sum[i] = right_total

        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left_sum[i] - right_sum[i + 1]
            min_diff = min(min_diff, diff)
        return min_diff