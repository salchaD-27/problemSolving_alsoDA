from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for num, cnt in count.items():
            if cnt > len(nums) // 3: ans.append(num)
        return ans