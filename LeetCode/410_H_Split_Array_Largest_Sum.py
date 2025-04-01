# from typing import List
# class Solution:
#     def splitArray(self, nums: List[int], k: int) -> int:
#         sum1=sum2=sum(nums)
#         for i in range(1, len(nums)-1):
#             arr1=nums[:i]
#             arr2=nums[i:]
#             tempsum1=sum(arr1)
#             tempsum2=sum(arr2)
#             if((tempsum1<sum1 and tempsum1<sum2)or(tempsum2<sum1 and tempsum2<sum2)):
#                 sum1=tempsum1
#                 sum2=tempsum2
#         return max(sum1, sum2)
    
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        
        def can_split(mid):
            count, current_sum = 1, 0
            for num in nums:
                if current_sum + num > mid:
                    count += 1
                    current_sum = num
                    if count > k: return False
                else: current_sum += num
            return True
        
        while left < right:
            mid = (left + right) // 2
            if can_split(mid): right = mid 
            else: left = mid + 1 
        return left