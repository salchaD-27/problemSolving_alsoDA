# from typing import List
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         def decreasing(nums, i):
#             for j in range(i, len(nums) - 1):
#                 if nums[j] < nums[j + 1]: return False
#             return True
#         # defaultCases
#         if(len(nums)==0 or len(nums)==1): return
#         # firstCase
#         temp = nums[:]
#         temp.sort()
#         if temp == nums:
#             nums[-1], nums[-2] = nums[-2], nums[-1]
#             return
#         # lastCase
#         temp = nums[:]
#         temp.sort(reverse=True)
#         if temp == nums:
#             nums.reverse()
#             return
#         # secondLastCase
#         lastIncreasingIndex = 0
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1] and decreasing(nums, i + 1):
#                 lastIncreasingIndex = i
#                 break
#         if(lastIncreasingIndex==1):
#             val = nums[-1]
#             nums.pop() 
#             nums.sort() 
#             nums.insert(0, val)  
#             return
#         # otherCases
#         lastIncreasingIndex = 0
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1] and decreasing(nums, i + 1):
#                 lastIncreasingIndex = i
#                 break
#         nums[lastIncreasingIndex - 1], nums[lastIncreasingIndex] = nums[lastIncreasingIndex], nums[lastIncreasingIndex - 1]
#         return

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1