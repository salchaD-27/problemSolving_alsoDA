# from typing import List
# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         seen=set()
#         score=0
#         for num in nums:
#             if num>0 and num not in seen:
#                 score+=num
#                 seen.add(num)
#         return score

# from typing import List
# class Solution:
#     def maxSum(self, nums: List[int]) -> int:
#         seen = set()
#         left = 0
#         curr_sum = 0
#         max_sum = 0
#         for right in range(len(nums)):
#             while nums[right] in seen:
#                 seen.remove(nums[left])
#                 curr_sum -= nums[left]
#                 left += 1
#             seen.add(nums[right])
#             curr_sum += nums[right]
#             max_sum = max(max_sum, curr_sum)
#         return max_sum

from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n < 0 for n in nums): return max(nums)
        unique = set(nums)
        return sum(n for n in unique if n > 0)

from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0 : return max(nums)
        else:
            result=0
            nums=set(nums)
            for i in nums:
                if i>=0: result+=i
            return result