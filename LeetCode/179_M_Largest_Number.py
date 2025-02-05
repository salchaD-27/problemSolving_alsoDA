# from typing import List
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         def toOnes(val):
#             afterDecimal=[]
#             while(val>10):
#                 temp=val%10
#                 afterDecimal.append(str(temp))
#                 val=val//10
#             afterDecimal.reverse()
#             tempAns=''
#             for num in afterDecimal:
#                 tempAns+=num
#             return str(val)+'.'+tempAns

#         for num in nums:
#             if(num>10): num=toOnes(num)
#             num=str(num)
#         nums.sort(reverse=True)
#         ans=''
#         for num in nums:
#             ans+=num
#         ans=ans.replace(".", "")
#         return ans

from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(key=lambda x: x*10, reverse=True)
        ans = "".join(nums)
        return "0" if ans[0] == "0" else ans