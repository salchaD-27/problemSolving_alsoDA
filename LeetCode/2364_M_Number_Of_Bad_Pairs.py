# from typing import List
# class Solution:
#     def countBadPairs(self, nums: List[int]) -> int:
#         ans=0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(i<j and (j-i)!=(nums[j]-nums[i])): ans+=1
#         return ans

from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        count_map = {} 
        good_pairs = 0
        for i in range(n):
            normalized = nums[i] - i
            if normalized in count_map:
                good_pairs += count_map[normalized]
                count_map[normalized] += 1
            else: count_map[normalized] = 1
        return total_pairs - good_pairs