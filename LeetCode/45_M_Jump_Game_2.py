# [2,3,1,1,4]
# find first max possible jump that directly reaches to last
# to find this we can start from end, and calculate till we find last value with arr[i]=n-i

# repeat this step for this new jump position
# repeat till first index

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                if i != n - 1:
                    jumps += 1
                    current_end = farthest
                else: break
        return jumps