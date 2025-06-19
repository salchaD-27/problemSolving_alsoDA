# from typing import List
# class Solution:
#     def partitionArray(self, nums: List[int], k: int) -> int:
#         notInSame=[[nums[0]]]
#         for i in range(1, len(nums)):
#             num=nums[i]
#             added=False
#             for j in range(len(notInSame)):
#                 tempMax=max(notInSame[j])
#                 tempMin=min(notInSame[j])
#                 if abs(tempMax-num)<=k and abs(tempMin-num)<=k:
#                     notInSame[j].append(num)
#                     added=True
#             if not added: notInSame.append([num])
#         return len(notInSame)

from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        start = nums[0]
        for num in nums:
            if num - start > k:
                count += 1
                start = num
        return count