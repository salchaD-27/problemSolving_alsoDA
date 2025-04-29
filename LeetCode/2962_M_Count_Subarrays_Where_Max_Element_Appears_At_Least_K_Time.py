# from typing import List
# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         maxElem = max(nums)
#         maxIndices = [i for i, num in enumerate(nums) if num == maxElem]
#         n = len(nums)
#         count = 0
#         for i in range(len(maxIndices) - k + 1):
#             left = maxIndices[i]
#             right = maxIndices[i + k - 1]
#             if i == 0: numStart = left + 1
#             else: numStart = left - maxIndices[i - 1]
#             if i + k == len(maxIndices): numEnd = n - right
#             else: numEnd = maxIndices[i + k] - right
#             count += numStart * numEnd
#         return count
    
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElem = max(nums)
        count = 0
        left = 0
        maxCount = 0
        for right in range(len(nums)):
            if nums[right] == maxElem: maxCount += 1
            while maxCount >= k:
                count += len(nums) - right
                if nums[left] == maxElem: maxCount -= 1
                left += 1
        return count