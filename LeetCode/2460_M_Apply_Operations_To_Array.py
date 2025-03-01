from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
        nonZeroNums = [num for num in nums if num != 0]
        zeroCount = len(nums) - len(nonZeroNums)
        return nonZeroNums + [0] * zeroCount