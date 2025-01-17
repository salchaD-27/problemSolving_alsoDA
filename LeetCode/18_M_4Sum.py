from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    temp=target-nums[k]-nums[j]-nums[i]
                    if(temp in nums[k+1:]): 
                        if([nums[i], nums[j], nums[k], temp] not in ans): ans.append([nums[i], nums[j], nums[k], temp])
        return ans