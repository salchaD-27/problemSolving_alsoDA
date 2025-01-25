from typing import List
from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)
        index = 0
        for num in sorted(numsCounter):
            for _ in range(min(numsCounter[num], 2)):
                nums[index] = num
                index += 1
        return index