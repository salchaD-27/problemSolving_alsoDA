from typing import List
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        return [num for num, count in count.items() if count==2]