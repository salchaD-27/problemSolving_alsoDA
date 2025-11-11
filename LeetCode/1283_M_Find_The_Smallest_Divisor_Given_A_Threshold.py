from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # for i in range(1,max(nums)+1):
        #     result=0
        #     for j in range(len(nums)):
        #         result=result+nums[j]//i
        #         if nums[j]%i!=0:
        #             result=result+1
        #     if result<=threshold:
        #         return i
        Low=1
        High=max(nums)
        Ans=10**7
        while(Low<=High):
            Mid=(Low+High)//2
            Result=0
            for i in range(len(nums)):
                Result=Result+nums[i]//Mid
                if nums[i]%Mid!=0: Result=Result+1
            if Result<=threshold:
                Ans=min(Mid,Ans)
                High=Mid-1
            else: Low=Mid+1
        return Ans