from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cantBe=[]
        for i in range(len(nums)-1):
            if((nums[i] not in nums[i+1:]) and (nums[i] not in cantBe)): return nums[i]
            else: cantBe.append(nums[i])
        return nums[-1]