from typing import List
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        N = len(nums)
        change = [1] * N
        for i in range(N): change[(i - nums[i] + 1) % N] -= 1
        for i in range(1, N): change[i] += change[i - 1]
        return change.index(max(change))