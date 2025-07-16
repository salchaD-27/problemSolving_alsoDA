from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        def maxSubseqLength(target_parity_func):
            length=1
            prev = nums[0]
            for i in range(1, len(nums)):
                if target_parity_func(prev, nums[i]):
                    length += 1
                    prev = nums[i]
            return length
        # case1: same parity, sum of adj must be even
        same_parity = lambda a, b: (a % 2) == (b % 2)
        # case2: alt parity, sum of adj must be odd
        alt_parity = lambda a, b: (a % 2) != (b % 2)
        return max(maxSubseqLength(same_parity), maxSubseqLength(alt_parity))

from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n=len(nums)
        if n==2: return 2
        z=nums[0]&1
        Len=[1-z, z, 1]
        for xx in nums[1:]:
            x=xx&1
            Len[x&1]+=1
            if x!=z:
                Len[2]+=1
                z=1-z
        return max(Len)