# from typing import List
# class Solution:
#     def smallestSubarrays(self, nums: List[int]) -> List[int]:
#         xorMap={}
#         res=[-1,-1]
#         resLen=0
#         prefixXORs=[nums[0]]
#         for i in range(1, len(nums)):
#             prefixXORs.append(prefixXORs[-1]^nums[i])
#         for i in range(len(nums)-1):
#             tempMaxXOR=nums[i]
#             tempMaxXORIdxs=[i,i]
#             XORlen=tempMaxXORIdxs[1]-tempMaxXORIdxs[0]+1
#             for j in range(i+1, len(nums)):
#                 tempXOR=prefixXORs[j]^prefixXORs[i-1]
#                 if tempXOR>tempMaxXOR or (tempXOR==tempMaxXOR and j-i+1<XORlen):
#                     tempMaxXOR=tempXOR
#                     tempMaxXORIdxs=[i,j]
#                     XORlen=tempMaxXORIdxs[1]-tempMaxXORIdxs[0]+1
#             if XORlen<resLen: res=tempMaxXORIdxs
#         return nums[res[0]:res[1]]

from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        last = [0] * 32  # last[i] - farthest idx where bit i is set
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b): last[b] = i
            # farthest idx needed to cover all set bits so far
            maxIdx = i
            for b in range(32):
                maxIdx = max(maxIdx, last[b])
            res[i] = maxIdx - i + 1
        return res