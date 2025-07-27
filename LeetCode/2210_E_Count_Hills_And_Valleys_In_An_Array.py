from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        high,low,cnt,n=0,0,0,len(nums)
        for i in range(1, n):
            if(nums[i] > nums[i - 1]):
                high=1
                if low:
                    cnt+=1
                    low=0
            elif(nums[i] < nums[i - 1]):
                low=1
                if high:
                    cnt+=1
                    high=0
        return int(cnt)