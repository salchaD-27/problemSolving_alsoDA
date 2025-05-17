# from typing import List
# class Solution:
#     def checkPossibility(self, nums: List[int]) -> bool:
#         outOfOrder=0
#         for i in range(len(nums)-1):
#             if nums[i]>=nums[i+1]: outOfOrder+=1
#         return False if outOfOrder>1 else True

from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if changed == 1: return False
                changed += 1
                if i < 2 or nums[i] >= nums[i - 2]: nums[i - 1] = nums[i]
                else: nums[i] = nums[i - 1]
        return True