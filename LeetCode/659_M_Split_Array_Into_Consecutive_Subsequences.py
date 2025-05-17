# from typing import List
# class Solution:
#     def isPossible(self, nums: List[int]) -> bool:
#         part1Last,part2Last=nums[0],-1
#         count1,count2=0,0
#         for i in range(1,len(nums)):
#             if nums[i]==part1Last+1: 
#                 part1last=nums[i]
#                 count1+=1
#             elif nums[i]==part1Last:
#                 if part2Last==-1 or nums[i]==part2Last+1: 
#                     part2last=nums[i]
#                     count2+=1
#                 elif nums[i]==part2Last: return False
#         return False if count1<3 or count2<3 else True

from typing import List
from collections import Counter, defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = defaultdict(int)
        for num in nums:
            if freq[num] == 0: continue
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            else: return False
            freq[num] -= 1
        return True