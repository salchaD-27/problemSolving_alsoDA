from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            prev2, prev1 = 0, 0
            for num in nums:
                new_pick = max(prev1, prev2 + num)
                prev2, prev1 = prev1, new_pick
            return prev1

        if not nums: return 0
        if len(nums)==1: return nums[0]
        if(1<len(nums)<4): return max(nums)
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        return max(case1, case2)