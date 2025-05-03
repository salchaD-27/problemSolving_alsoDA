from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        def get_sequence_starts(arr):
            starts = []
            n = len(arr)
            for i in range(n):
                if i == 0 or arr[i] != arr[i-1] + 1: starts.append(arr[i])
            return starts

        # nums = [1000,100,10,2]
        # nums = [2,3,4]
        # nums = [1000,100,10,2,345,643,47,432]
        tempNums=nums
        parenStarts=[]
        # iterCount=0
        while(len(tempNums)>2):
            dp=[0]*(len(tempNums)-1)
            for i in range(len(tempNums)-1):
                dp[i]=tempNums[i]/tempNums[i+1]
            maxQ=0
            maxIdx=0
            for i in range(len(dp)):
                if(dp[i]>=maxQ):
                    maxQ=dp[i]
                    maxIdx=i
            # parenStarts.append(i+iterCount)
            parenStarts.append(i)
            tempNums=tempNums[:maxIdx]+tempNums[maxIdx+1:]
            # iterCount+=1
        parenStarts.sort()
        parenStarts=get_sequence_starts(parenStarts)
        for i in range(len(parenStarts)):
            nums.insert(parenStarts[i],'(')
        resStr=''
        for i in range(len(nums)):
            if(nums[i]!='(' and i!=len(nums)-1): resStr+=str(nums[i])+'/'
            else: resStr+=str(nums[i])
        resStr+=')'*len(parenStarts)

        return resStr
    

# illegal math shortcut
from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1: return str(nums[0])
        if len(nums) == 2: return f"{nums[0]}/{nums[1]}"
        middle = "/".join(map(str, nums[1:]))
        return f"{nums[0]}/({middle})"